import streamlit as st

st.set_page_config(
    page_title="Explainable AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable AI")

st.markdown("""
This page explains how the LightGBM model makes predictions using SHAP (SHapley Additive exPlanations).

SHAP values measure the contribution of each feature towards the predicted property price.
""")

st.markdown("---")

st.subheader("SHAP Summary Plot")

st.image(
    "shap_summary.png",
    use_container_width=True
)

st.info("""
Features at the top of the SHAP summary have the greatest influence on property price predictions.
""")
