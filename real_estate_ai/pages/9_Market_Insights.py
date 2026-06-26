import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Market Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Market Insights")

@st.cache_data
def load_data():
    return pd.read_csv("property_master.csv")

df = load_data()

# ------------------------------------
# KPI Cards
# ------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Properties", len(df))
c2.metric("Cities", df["city"].nunique())
c3.metric("Localities", df["locality"].nunique())
c4.metric("Avg Price", f"₹{df['price'].mean():,.0f}")

st.markdown("---")

# ------------------------------------
# Average Price by City
# ------------------------------------

st.subheader("Average Property Price by City")

city_price = (

    df.groupby("city")["price"]

      .mean()

      .sort_values(ascending=False)

      .reset_index()

)

fig = px.bar(

    city_price,

    x="city",

    y="price",

    color="price",

    title="Average Price by City"

)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------
# Top 10 Localities
# ------------------------------------

st.subheader("Top 10 Localities by Average Price")

top_localities = (

    df.groupby("locality")["price"]

      .mean()

      .sort_values(ascending=False)

      .head(10)

      .reset_index()

)

fig = px.bar(

    top_localities,

    x="locality",

    y="price",

    color="price"

)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------
# Average Property Price by Type
# ------------------------------------

st.subheader("Property Type Analysis")

ptype = (

    df.groupby("property_type")["price"]

      .mean()

      .reset_index()

)

fig = px.pie(

    ptype,

    names="property_type",

    values="price",

    title="Average Price by Property Type"

)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------
# Price Distribution
# ------------------------------------

st.subheader("Price Distribution")

fig = px.box(

    df,

    y="price",

    color="city"

)

st.plotly_chart(fig, use_container_width=True)

st.success("Market Insights Generated Successfully")
