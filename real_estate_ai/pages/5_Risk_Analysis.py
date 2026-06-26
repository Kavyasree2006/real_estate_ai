import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Property Risk Analysis")

# --------------------------
# Load Dataset
# --------------------------

@st.cache_data
def load_data():
    return pd.read_csv("investment_recommendations.csv")

df = load_data()

# --------------------------
# Overview
# --------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Risk",
    round(df["risk_score"].mean(),2)
)

col2.metric(
    "Maximum Risk",
    round(df["risk_score"].max(),2)
)

col3.metric(
    "Minimum Risk",
    round(df["risk_score"].min(),2)
)

st.markdown("---")

# --------------------------
# Risk Distribution
# --------------------------

st.subheader("Risk Score Distribution")

fig = px.histogram(
    df,
    x="risk_score",
    nbins=30,
    title="Distribution of Risk Scores"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------
# Risk Categories
# --------------------------

def category(score):

    if score < 35:
        return "Low Risk"

    elif score < 65:
        return "Medium Risk"

    else:
        return "High Risk"

df["Risk Category"] = df["risk_score"].apply(category)

st.subheader("Risk Categories")

fig = px.pie(
    df,
    names="Risk Category",
    title="Property Risk Categories"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------
# Highest Risk Properties
# --------------------------

st.subheader("Highest Risk Properties")

st.dataframe(

    df.sort_values(
        "risk_score",
        ascending=False
    ).head(20)

)

# --------------------------
# Lowest Risk Properties
# --------------------------

st.subheader("Lowest Risk Properties")

st.dataframe(

    df.sort_values(
        "risk_score"
    ).head(20)

)

# --------------------------
# ROI vs Risk
# --------------------------

st.subheader("ROI vs Risk")

fig = px.scatter(

    df,

    x="risk_score",

    y="roi_percent",

    color="recommendation",

    hover_data=["price","predicted_price"]

)

st.plotly_chart(fig,use_container_width=True)

st.success("Risk Analysis Completed")
