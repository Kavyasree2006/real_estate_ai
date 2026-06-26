import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="EDA Dashboard", page_icon="📊")

st.title("📊 Exploratory Data Analysis Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("property_master.csv")

df = load_data()

st.markdown("---")

# ===============================
# KPI Cards
# ===============================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Properties", f"{len(df):,}")
col2.metric("Average Price", f"₹{df['price'].mean():,.0f}")
col3.metric("Average Area", f"{df['area_sqft'].mean():,.0f} sqft")
col4.metric("Cities", df["city"].nunique())

st.markdown("---")

# ===============================
# Dataset Preview
# ===============================

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.markdown("---")

# ===============================
# Price Distribution
# ===============================

st.subheader("Price Distribution")

fig = px.histogram(
    df,
    x="price",
    nbins=50,
    title="Distribution of Property Prices"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Area Distribution
# ===============================

st.subheader("Area Distribution")

fig = px.histogram(
    df,
    x="area_sqft",
    nbins=40,
    title="Distribution of Property Area"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Area vs Price
# ===============================

st.subheader("Area vs Price")

fig = px.scatter(
    df,
    x="area_sqft",
    y="price",
    color="city",
    hover_data=["bhk"],
    title="Area vs Price"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# BHK Distribution
# ===============================

st.subheader("BHK Distribution")

fig = px.histogram(
    df,
    x="bhk",
    title="BHK Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# City Distribution
# ===============================

st.subheader("Properties by City")

city_counts = df["city"].value_counts()

fig = px.bar(
    city_counts,
    title="Properties Available in Each City"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Property Type Distribution
# ===============================

st.subheader("Property Type Distribution")

ptype = df["property_type"].value_counts()

fig = px.pie(
    values=ptype.values,
    names=ptype.index,
    title="Property Types"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Correlation Heatmap
# ===============================

st.subheader("Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(10,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.markdown("---")

st.success("EDA Completed Successfully")
