import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Property Price Prediction", page_icon="🏠")

st.title("🏠 Property Price Prediction")

# -------------------------------
# Load Model
# -------------------------------

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# -------------------------------
# User Inputs
# -------------------------------

st.subheader("Enter Property Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sqft)",
        min_value=100,
        max_value=20000,
        value=1200
    )

    bhk = st.selectbox(
        "BHK",
        [1,2,3,4,5,6]
    )

    bathrooms = st.selectbox(
        "Bathrooms",
        [1,2,3,4,5,6]
    )

    balconies = st.selectbox(
        "Balconies",
        [0,1,2,3,4]
    )

    property_age = st.slider(
        "Property Age",
        0,
        50,
        5
    )

with col2:

    total_floor = st.number_input(
        "Total Floors",
        1,
        80,
        10
    )

    floor_number = st.number_input(
        "Floor Number",
        0,
        80,
        3
    )

    furnished_status = st.selectbox(
        "Furnished Status",
        [0,1]
    )

    population_score = st.slider(
        "Population Score",
        0,
        100,
        70
    )

    healthcare_score = st.slider(
        "Healthcare Score",
        0,
        100,
        75
    )

road_score = st.slider(
    "Road Score",
    0,
    100,
    70
)

city = st.selectbox(
    "City",
    [
        "Other",
        "SOUTH MUMBAI",
        "HYDERABAD"
    ]
)

locality = st.selectbox(
    "Locality",
    [
        "Other",
        "Sector 62 Gurgaon",
        "Sector 59 Gurgaon",
        "Sector 54 Gurgaon",
        "Sector 108 Gurgaon",
        "Sector 67 Gurgaon"
    ]
)

property_type = st.selectbox(
    "Property Type",
    [
        "Apartment",
        "Independent House/Villa",
        "Residential Land"
    ]
)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Property Price"):

    sample = pd.DataFrame({

        "healthcare_score":[healthcare_score],
        "population_score":[population_score],
        "bhk":[bhk],
        "bathrooms":[bathrooms],
        "total_floor":[total_floor],
        "furnished_status":[furnished_status],
        "area_sqft":[area],
        "floor_number":[floor_number],
        "property_age":[property_age],
        "road_score":[road_score],
        "balconies":[balconies],

        "locality_Sector 62 Gurgaon":[1 if locality=="Sector 62 Gurgaon" else 0],

        "city_SOUTH MUMBAI":[1 if city=="SOUTH MUMBAI" else 0],

        "city_HYDERABAD":[1 if city=="HYDERABAD" else 0],

        "property_type_Independent House/Villa":[1 if property_type=="Independent House/Villa" else 0],

        "locality_Sector 59 Gurgaon":[1 if locality=="Sector 59 Gurgaon" else 0],

        "property_type_Residential Land":[1 if property_type=="Residential Land" else 0],

        "locality_Sector 54 Gurgaon":[1 if locality=="Sector 54 Gurgaon" else 0],

        "locality_Sector 108 Gurgaon":[1 if locality=="Sector 108 Gurgaon" else 0],

        "locality_Sector 67 Gurgaon":[1 if locality=="Sector 67 Gurgaon" else 0]

    })

    prediction = model.predict(sample)[0]

    st.success(f"### 💰 Predicted Property Price")

    st.metric(
        "Estimated Price",
        f"₹ {prediction:,.0f}"
    )

    st.balloons()

    st.markdown("---")

    st.write("### Input Summary")

    st.dataframe(sample)
