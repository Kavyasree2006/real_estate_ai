import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Future Forecast",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Future Property Price Forecast")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("future_price_forecasts.csv")

df = load_data()

# --------------------------------------------------
# KPIs
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Avg Price",
    f"₹{df['predicted_price'].mean():,.0f}"
)

col2.metric(
    "1 Year Forecast",
    f"₹{df['forecast_1yr'].mean():,.0f}"
)

col3.metric(
    "3 Year Forecast",
    f"₹{df['forecast_3yr'].mean():,.0f}"
)

col4.metric(
    "5 Year Forecast",
    f"₹{df['forecast_5yr'].mean():,.0f}"
)

st.markdown("---")

# --------------------------------------------------
# Forecast Table
# --------------------------------------------------

st.subheader("Forecast Dataset")

st.dataframe(df.head(20), use_container_width=True)

# --------------------------------------------------
# Average Forecast Comparison
# --------------------------------------------------

forecast_summary = pd.DataFrame({

    "Year":[
        "Current",
        "1 Year",
        "3 Years",
        "5 Years"
    ],

    "Average Price":[

        df["predicted_price"].mean(),

        df["forecast_1yr"].mean(),

        df["forecast_3yr"].mean(),

        df["forecast_5yr"].mean()

    ]

})

fig = px.bar(

    forecast_summary,

    x="Year",

    y="Average Price",

    text_auto=".2s",

    title="Average Future Price Forecast"

)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Individual Property Forecast
# --------------------------------------------------

st.subheader("Property Forecast")

index = st.slider(

    "Select Property",

    0,

    len(df)-1,

    0

)

sample = df.iloc[index]

forecast = pd.DataFrame({

    "Year":[
        "Current",
        "1 Year",
        "3 Years",
        "5 Years"
    ],

    "Price":[

        sample["predicted_price"],

        sample["forecast_1yr"],

        sample["forecast_3yr"],

        sample["forecast_5yr"]

    ]

})

fig = px.line(

    forecast,

    x="Year",

    y="Price",

    markers=True,

    title="Future Price Growth"

)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Growth Rate Distribution
# --------------------------------------------------

st.subheader("Growth Rate Distribution")

fig = px.histogram(

    df,

    x="growth_rate",

    nbins=30,

    title="Growth Rate Distribution"

)

st.plotly_chart(fig, use_container_width=True)

st.success("Forecast Analysis Completed Successfully")
