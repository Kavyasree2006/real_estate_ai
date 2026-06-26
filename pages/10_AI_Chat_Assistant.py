import streamlit as st
import pandas as pd
from groq import Groq

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Real Estate Chat Assistant")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

investment = pd.read_csv("investment_recommendations.csv")
forecast = pd.read_csv("future_price_forecasts.csv")

context = f"""
You are an AI Real Estate Investment Advisor.

Project Statistics:

Average Property Price:
₹{investment['price'].mean():,.0f}

Average Predicted Price:
₹{investment['predicted_price'].mean():,.0f}

Average ROI:
{investment['roi_percent'].mean():.2f}%

Average Risk Score:
{investment['risk_score'].mean():.2f}

BUY Recommendations:
{(investment['recommendation']=="BUY").sum()}

HOLD Recommendations:
{(investment['recommendation']=="HOLD").sum()}

SELL Recommendations:
{(investment['recommendation']=="SELL").sum()}

Average 5-Year Forecast Price:
₹{forecast['forecast_5yr'].mean():,.0f}

Answer using only this project information.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask anything about real estate...")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":context
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
