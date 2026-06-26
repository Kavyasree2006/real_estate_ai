import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Investment Recommendation",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Investment Recommendation Engine")

# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv("investment_recommendations.csv")

df = load_data()

st.markdown("---")

# -----------------------------
# Dataset Overview
# -----------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Properties", len(df))

if "recommendation" in df.columns:
    col2.metric(
        "BUY Recommendations",
        (df["recommendation"] == "BUY").sum()
    )

if "city" in df.columns:
    col3.metric(
        "Cities",
        df["city"].nunique()
    )

st.markdown("---")

# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Filter Properties")

filtered = df.copy()

if "city" in df.columns:

    cities = sorted(df["city"].dropna().unique())

    selected_city = st.sidebar.selectbox(
        "Select City",
        ["All"] + cities
    )

    if selected_city != "All":
        filtered = filtered[
            filtered["city"] == selected_city
        ]

if "property_type" in df.columns:

    types = sorted(df["property_type"].dropna().unique())

    selected_type = st.sidebar.selectbox(
        "Property Type",
        ["All"] + types
    )

    if selected_type != "All":
        filtered = filtered[
            filtered["property_type"] == selected_type
        ]

# -----------------------------
# Recommendation Summary
# -----------------------------

st.subheader("Recommendation Summary")

if "recommendation" in filtered.columns:

    fig = px.histogram(
        filtered,
        x="recommendation",
        color="recommendation",
        title="Recommendation Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Top Recommended Properties
# -----------------------------

st.subheader("Top Recommended Properties")

st.dataframe(
    filtered.head(20),
    use_container_width=True
)

# -----------------------------
# Price Distribution
# -----------------------------

if "price" in filtered.columns:

    st.subheader("Property Price Distribution")

    fig = px.histogram(
        filtered,
        x="price",
        nbins=30,
        title="Price Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Area vs Price
# -----------------------------

if (
    "area_sqft" in filtered.columns
    and
    "price" in filtered.columns
):

    st.subheader("Area vs Price")

    fig = px.scatter(
        filtered,
        x="area_sqft",
        y="price",
        color="recommendation"
        if "recommendation" in filtered.columns
        else None,
        hover_data=filtered.columns
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Download
# -----------------------------

csv = filtered.to_csv(index=False)

st.download_button(
    label="📥 Download Recommendations",
    data=csv,
    file_name="filtered_recommendations.csv",
    mime="text/csv"
)

st.success("Investment recommendations loaded successfully.")
