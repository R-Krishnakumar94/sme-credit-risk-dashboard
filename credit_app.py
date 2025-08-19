# === SME CREDIT RISK SCORING DASHBOARD ===

import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import joblib

# === TITLE & INSTRUCTIONS ===
st.title("💳 SME Credit Risk Scoring Dashboard")
st.write("Upload SME financial data to predict credit risk using a trained AI model.")

# === FILE UPLOAD ===
uploaded_file = st.file_uploader("📤 Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # === CLEANING: Drop non-feature columns (if present) ===
    X = df.drop(columns=["Business_ID", "risk_label", "default_risk_score"], errors="ignore")

    # === LOAD SAVED MODEL ===
    model = joblib.load("xgb_credit_model.pkl")

    # === MAKE PREDICTIONS ===
    predictions = model.predict(X)
    df["Predicted_Risk"] = np.where(predictions == 1, "❗ High Risk", "✅ Low Risk")

    # === BAR CHART: Risk Distribution ===
    st.subheader("📊 Risk Category Summary")
    risk_counts = df["Predicted_Risk"].value_counts()
    st.bar_chart(risk_counts)

    # === SHOW FULL RESULTS ===
    st.subheader("🔎 All Predictions")
    st.dataframe(df[["Business_ID", "Predicted_Risk"]])

    # === HIGHLIGHT HIGH-RISK SMEs ===
    st.subheader("🚨 High Risk SMEs Only")
    st.dataframe(df[df["Predicted_Risk"] == "❗ High Risk"])
