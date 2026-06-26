import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Property Comparison",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Property Comparison")

@st.cache_data
def load_data():
    return pd.read_csv("property_master.csv")

df = load_data()

st.subheader("Select Two Properties")

col1, col2 = st.columns(2)

with col1:
    property1 = st.selectbox(
        "Property A",
        df.index,
        format_func=lambda x: f"Property {x}"
    )

with col2:
    property2 = st.selectbox(
        "Property B",
        df.index,
        index=1,
        format_func=lambda x: f"Property {x}"
    )

p1 = df.loc[property1]
p2 = df.loc[property2]

comparison = pd.DataFrame({

    "Feature":[
        "Price",
        "Area",
        "BHK",
        "Bathrooms",
        "Balconies",
        "Property Age"
    ],

    "Property A":[
        p1["price"],
        p1["area_sqft"],
        p1["bhk"],
        p1["bathrooms"],
        p1["balconies"],
        p1["property_age"]
    ],

    "Property B":[
        p2["price"],
        p2["area_sqft"],
        p2["bhk"],
        p2["bathrooms"],
        p2["balconies"],
        p2["property_age"]
    ]

})

st.dataframe(
    comparison,
    use_container_width=True
)

fig = go.Figure()

fig.add_trace(go.Bar(
    name="Property A",
    x=comparison["Feature"],
    y=comparison["Property A"]
))

fig.add_trace(go.Bar(
    name="Property B",
    x=comparison["Feature"],
    y=comparison["Property B"]
))

fig.update_layout(
    barmode="group",
    title="Property Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Comparison Completed Successfully")
