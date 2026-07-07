# 🏠 AI Powered Real Estate Analytics Platform Using Machine Learning

> An end-to-end AI-powered real estate analytics platform that predicts property prices, evaluates investment opportunities, analyzes risk, forecasts future property values, explains model predictions using SHAP, and provides an interactive Streamlit dashboard.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![LightGBM](https://img.shields.io/badge/LightGBM-ML-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

# 📌 Project Overview

The **AI Powered Real Estate Analytics Platform** is an intelligent decision-support system designed to assist property buyers, investors, and real estate professionals in making data-driven investment decisions.

The platform combines **Machine Learning**, **Explainable AI**, **Risk Analysis**, **Forecasting**, and **Interactive Visualization** into a single Streamlit web application.

Unlike traditional property evaluation systems, this platform provides:

- AI-based property price prediction
- Investment recommendations
- Property risk assessment
- Future price forecasting
- Explainable AI using SHAP
- Property comparison
- Market insights
- AI Chat Assistant
- Real-Time Property Analyzer
- Property Ranking System

---

# 🚀 Features

## 🏠 Property Price Prediction

Predicts the market value of residential properties using a trained **LightGBM Regression Model**.

Input Features include:

- Area
- BHK
- Bathrooms
- Property Age
- Furnished Status
- Infrastructure Score
- Road Score
- Population Score
- Healthcare Score
- Floor Information
- Location Information

---

## 📈 Investment Recommendation

Automatically recommends:

- ✅ BUY
- ⚠ HOLD
- ❌ SELL

Recommendation is generated using:

- Predicted Price
- ROI Percentage
- Risk Score

---

## ⚠ Risk Analysis

Evaluates investment risk using:

- Crime Index
- Property Age
- Infrastructure Score
- Market Volatility

Risk Categories:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

---

## 📊 Future Price Forecasting

Forecasts property prices for:

- 1 Year
- 3 Years
- 5 Years

Forecasting is performed using a **Compound Growth Model** based on infrastructure and development indicators.

---

## 🧠 Explainable AI (SHAP)

Explains model predictions using SHAP.

Provides:

- Feature Importance
- Global Explanation
- Local Explanation
- Model Transparency

---

## 📈 Market Insights

Interactive dashboards including:

- Average Price by City
- Top Investment Areas
- Property Type Analysis
- Price Distribution
- Area Distribution

---

## 🏡 Property Comparison

Allows comparison between two different properties based on:

- Area
- Price
- BHK
- Bathrooms
- Balconies
- Property Age

---

## 🤖 AI Chat Assistant

Interactive chatbot capable of answering real estate questions such as:

- Should I invest in this property?
- What affects property prices?
- Explain ROI
- Explain Risk Score
- Explain SHAP

---

## 📂 Real-Time Property Analyzer

Users can upload a CSV file containing property information.

The application automatically generates:

- Predicted Price
- Risk Score
- ROI
- Investment Recommendation

---

## 🏆 Property Ranking System

Automatically ranks the **Top 10 Investment Properties** based on:

- ROI
- Risk Score
- Predicted Price

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Dashboard |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| LightGBM | Regression Model |
| SHAP | Explainable AI |
| Plotly | Interactive Charts |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Joblib / Pickle | Model Serialization |

---

# 📂 Project Structure

```
real_estate_ai/
│
├── app.py
├── requirements.txt
├── model.pkl
├── property_master.csv
├── investment_recommendations.csv
├── future_price_forecasts.csv
├── shap_summary.png
│
├── pages/
│   ├── 1_Project_Overview.py
│   ├── 2_EDA_Dashboard.py
│   ├── 3_Price_Prediction.py
│   ├── 4_Investment_Recommendation.py
│   ├── 5_Risk_Analysis.py
│   ├── 6_Future_Forecast.py
│   ├── 7_Explainable_AI.py
│   ├── 8_Property_Comparison.py
│   ├── 9_Market_Insights.py
│   ├── 10_AI_Chat_Assistant.py
│   ├── 11_Real_Time_Property_Analyzer.py
│   └── 12_Property_Ranking_System.py
│
└── README.md
```

---

# 📊 Dataset

The dataset contains residential property information collected from multiple locations.

### Features

- City
- Locality
- Property Type
- Area (sq.ft.)
- BHK
- Bathrooms
- Balconies
- Floor Number
- Total Floors
- Property Age
- Furnished Status
- Infrastructure Score
- Healthcare Score
- Population Score
- Road Score
- Crime Index
- Property Price

---

# 🔄 Project Workflow

```
Property Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Machine Learning Models
        │
        ▼
Model Evaluation
        │
        ▼
LightGBM (Best Model)
        │
        ▼
Price Prediction
        │
        ▼
Investment Recommendation
        │
        ▼
Risk Analysis
        │
        ▼
Future Price Forecast
        │
        ▼
Explainable AI (SHAP)
        │
        ▼
Interactive Streamlit Dashboard
```

---

# 🤖 Machine Learning Models

The following regression models were evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- **LightGBM Regressor (Best Model)**

### Best Model

**LightGBM**

Performance:

| Metric | Value |
|----------|------------|
| MAE | 3,279,884.66 |
| RMSE | 5,900,424.01 |
| R² Score | 0.7128 |

---

# 📈 Feature Engineering

Engineered features include:

- Infrastructure Score
- Growth Rate
- Predicted Price
- ROI Percentage
- Risk Score
- Recommendation
- Future Forecast Prices

---

# 📊 Explainable AI

The project integrates **SHAP (SHapley Additive exPlanations)** to improve transparency.

Capabilities include:

- Feature Importance
- Global Model Interpretation
- Local Prediction Explanation

---

# 💻 Streamlit Dashboard

The dashboard includes the following modules:

- 🏠 Home
- 📄 Project Overview
- 📊 EDA Dashboard
- 💰 Property Price Prediction
- 📈 Investment Recommendation
- ⚠ Risk Analysis
- 📅 Future Forecast
- 🧠 Explainable AI
- 🏡 Property Comparison
- 📊 Market Insights
- 🤖 AI Chat Assistant
- 📂 Real-Time Property Analyzer
- 🏆 Property Ranking System

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/real_estate_ai.git
```

Move into the project folder

```bash
cd real_estate_ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Application Screenshots

## Home Page

<img width="1366" height="768" alt="Screenshot (263)" src="https://github.com/user-attachments/assets/4bc2c6a7-4486-486d-94bc-58a21aede901" />

---

## EDA Dashboard

<img width="1366" height="768" alt="Screenshot (264)" src="https://github.com/user-attachments/assets/0748903c-c7e8-4c19-a973-4a64fda42196" />

---

## Price Prediction

<img width="1366" height="768" alt="Screenshot (265)" src="https://github.com/user-attachments/assets/971dda4d-af48-4a36-820d-e9793b836c03" />

---

## Investment Recommendation

<img width="1366" height="768" alt="Screenshot (266)" src="https://github.com/user-attachments/assets/b0ff5f73-d831-4000-b8e6-e943722eb61f" />

---

## Risk Analysis

<img width="1366" height="768" alt="Screenshot (267)" src="https://github.com/user-attachments/assets/e88fc275-16c4-419a-af20-c32721c76214" />

---

## Future Forecast

<img width="1366" height="768" alt="Screenshot (268)" src="https://github.com/user-attachments/assets/8bd6e268-d564-4688-85b2-073e69430be7" />

---

## SHAP Explainability

<img width="1366" height="768" alt="Screenshot (269)" src="https://github.com/user-attachments/assets/b438eff0-ce8f-4d48-8b58-ecc4ca318994" />

---

## AI Chat Assistant

<img width="1366" height="768" alt="Screenshot (270)" src="https://github.com/user-attachments/assets/e3ea08ca-cc6a-474b-bec2-0ad97a3f5643" />

---

## Property Ranking

<img width="1366" height="768" alt="Screenshot (271)" src="https://github.com/user-attachments/assets/9257b7da-d268-4a1f-9dee-749d1aaa4344" />

---

# 📈 Future Enhancements

- Live Real Estate API Integration
- GIS-Based Property Mapping
- Mobile Application
- User Authentication
- Personalized Property Recommendations
- Time-Series Forecasting
- Advanced AI Chatbot with LLM Integration
- Cloud Database Integration
- Multi-Language Support

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

- Machine Learning Regression
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Explainable AI (SHAP)
- Risk Analysis
- Forecasting Techniques
- Streamlit Dashboard Development
- Interactive Data Visualization
- AI-based Decision Support Systems

---

# 👨‍💻 Author

**K. Kavya Sree**

Internship Project

AI Powered Real Estate Analytics Platform Using Machine Learning

---

# 📄 License

This project is developed for **educational and internship purposes**.

---

# ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐** on GitHub.
