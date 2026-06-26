import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Property Ranking System",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Property Ranking System")

@st.cache_data
def load_data():
    return pd.read_csv("investment_recommendations.csv")

df = load_data()

# ------------------------------------------------
# Normalize Scores
# ------------------------------------------------

# Higher ROI is better
df["roi_score"] = (
    (df["roi_percent"] - df["roi_percent"].min()) /
    (df["roi_percent"].max() - df["roi_percent"].min())
) * 100

# Lower Risk is better
df["risk_score_normalized"] = (
    100 -
    (
        (df["risk_score"] - df["risk_score"].min()) /
        (df["risk_score"].max() - df["risk_score"].min())
    ) * 100
)

# Higher Predicted Price is better
df["price_score"] = (
    (df["predicted_price"] - df["predicted_price"].min()) /
    (df["predicted_price"].max() - df["predicted_price"].min())
) * 100

# ------------------------------------------------
# Final Ranking Score
# ------------------------------------------------

df["Ranking Score"] = (
      0.50 * df["roi_score"]
    + 0.30 * df["risk_score_normalized"]
    + 0.20 * df["price_score"]
)

# ------------------------------------------------
# Rank Properties
# ------------------------------------------------

df = df.sort_values(
    "Ranking Score",
    ascending=False
)

df["Rank"] = range(1, len(df)+1)

top10 = df.head(10)

# ------------------------------------------------
# KPI Cards
# ------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric("Total Properties", len(df))
c2.metric("Top Ranked Score", f"{top10.iloc[0]['Ranking Score']:.2f}")
c3.metric("Average ROI", f"{df['roi_percent'].mean():.2f}%")

st.markdown("---")

# ------------------------------------------------
# Top 10 Table
# ------------------------------------------------

st.subheader("🏆 Top 10 Investment Properties")

st.dataframe(
    top10[
        [
            "Rank",
            "predicted_price",
            "roi_percent",
            "risk_score",
            "recommendation",
            "Ranking Score"
        ]
    ],
    use_container_width=True
)

# ------------------------------------------------
# Ranking Chart
# ------------------------------------------------

fig = px.bar(
    top10,
    x="Rank",
    y="Ranking Score",
    color="recommendation",
    hover_data=[
        "predicted_price",
        "roi_percent",
        "risk_score"
    ],
    title="Top 10 Property Rankings"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------
# Download
# ------------------------------------------------

csv = top10.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Top 10 Properties",
    csv,
    "Top10_Properties.csv",
    "text/csv"
)

st.success("Property Ranking Completed Successfully")
