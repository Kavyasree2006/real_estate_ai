import streamlit as st

st.set_page_config(page_title="Project Overview", page_icon="📋")

st.title("📋 AI Powered Real Estate Analytics Platform")

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
This project leverages Artificial Intelligence and Machine Learning to
analyze real estate data, predict property prices, recommend investment
opportunities, assess property risk, and forecast future market trends.

The system is designed to assist investors, buyers, and real estate
professionals in making data-driven decisions.
""")

st.markdown("---")

st.header("🚀 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Programming
- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
    """)

with col2:
    st.markdown("""
### Visualization
- Streamlit
- Matplotlib
- Seaborn
- Plotly
- SHAP
    """)

st.markdown("---")

st.header("📊 Modules")

st.success("✅ Exploratory Data Analysis")

st.success("✅ Feature Engineering")

st.success("✅ Property Price Prediction")

st.success("✅ Investment Recommendation")

st.success("✅ Risk Analysis")

st.success("✅ Future Price Forecasting")

st.success("✅ Explainable AI (SHAP)")

st.success("✅ Property Comparison")

st.success("✅ Market Insights")

st.markdown("---")

st.header("📈 Model Performance")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Model", "LightGBM")
c2.metric("R² Score", "0.713")
c3.metric("Features", "20")
c4.metric("Training Samples", "28,672")

st.markdown("---")

st.info(
    "Use the navigation menu on the left to explore the dashboard pages."
)
