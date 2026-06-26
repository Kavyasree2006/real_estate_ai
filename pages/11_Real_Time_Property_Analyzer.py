import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Real-Time Property Analyzer",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Real-Time Property Analyzer")

st.write(
    "Upload a CSV file containing property details to predict prices, estimate risk, and receive investment recommendations."
)

# Load model
model = pickle.load(open("model.pkl", "rb"))

uploaded_file = st.file_uploader(
    "Upload Property CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    # Required model features
    selected_features = [
        'healthcare_score',
        'population_score',
        'bhk',
        'bathrooms',
        'total_floor',
        'furnished_status',
        'area_sqft',
        'floor_number',
        'property_age',
        'road_score',
        'balconies',
        'locality_Sector 62 Gurgaon',
        'city_SOUTH MUMBAI',
        'city_HYDERABAD',
        'property_type_Independent House/Villa',
        'locality_Sector 59 Gurgaon',
        'property_type_Residential Land',
        'locality_Sector 54 Gurgaon',
        'locality_Sector 108 Gurgaon',
        'locality_Sector 67 Gurgaon'
    ]

    missing = [c for c in selected_features if c not in df.columns]

    if missing:
        st.error("Missing required columns:")
        st.write(missing)

    else:

        X = df[selected_features]

        df["Predicted Price"] = model.predict(X)

        # Example risk score
        if {"crime_index", "infrastructure_score", "property_age"}.issubset(df.columns):

            df["Risk Score"] = (
                0.4 * df["crime_index"] +
                0.3 * df["property_age"] +
                0.3 * (100 - df["infrastructure_score"])
            )

        else:
            df["Risk Score"] = 50

        # ROI
        if "price" in df.columns:
            df["ROI %"] = (
                (df["Predicted Price"] - df["price"])
                / df["price"]
            ) * 100
        else:
            df["ROI %"] = 0

        # Recommendation
        def recommend(row):
            if row["ROI %"] > 15 and row["Risk Score"] < 40:
                return "BUY"
            elif row["ROI %"] > 5:
                return "HOLD"
            else:
                return "SELL"

        df["Recommendation"] = df.apply(recommend, axis=1)

        st.subheader("Analysis Results")

        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Results",
            csv,
            "property_analysis_results.csv",
            "text/csv"
        )
