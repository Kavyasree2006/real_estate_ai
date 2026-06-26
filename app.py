# paste the app.py code here
import streamlit as st

st.set_page_config(
    page_title="AI Powered Real Estate Analytics Platform",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 AI Powered Real Estate Analytics Platform")

st.markdown("---")

st.markdown("""
### Welcome

This dashboard demonstrates an AI-powered real estate analytics system built using Machine Learning and Explainable AI.

### Modules Included

✅ Project Overview

✅ Exploratory Data Analysis

✅ Property Price Prediction

✅ Investment Recommendation

✅ Risk Analysis

✅ Future Price Forecasting

✅ Explainable AI (SHAP)

✅ Property Comparison

✅ Market Insights

---

### Model Used

- LightGBM Regressor
- R² Score ≈ **0.71**
- Explainable AI using SHAP

Use the **left sidebar** to navigate between pages.
""")

col1, col2, col3 = st.columns(3)

col1.metric("Model", "LightGBM")
col2.metric("Features", "20")
col3.metric("R² Score", "0.713")
