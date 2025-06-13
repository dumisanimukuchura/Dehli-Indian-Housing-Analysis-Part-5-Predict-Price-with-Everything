# app.py
import streamlit as st
import pandas as pd
import joblib

# --- Load Model ---
model = joblib.load("dehli_rent_prediction_model.pkl")

# --- Load Data for UI Options ---
df = pd.read_csv("Dehli-Indian-Housing-Clean-Data.csv")

# --- Clean for UI Use ---
df = df[["house_size_in_sqft", "location", "house_type"]].dropna()
locations = sorted(df["location"].unique())
house_types = sorted(df["house_type"].unique())
min_size = int(df["house_size_in_sqft"].min())
max_size = int(df["house_size_in_sqft"].max())
default_size = int(df["house_size_in_sqft"].mean())

# --- Streamlit UI ---
st.set_page_config(page_title="Delhi Housing Price Prediction", layout="centered")
st.title("🏠 New Delhi Housing Price Prediction")
st.markdown("Use the sliders and dropdowns below to estimate the rental price of a property.")

# --- Inputs ---
house_size = st.slider("📏 House Size (sqft)", min_value=min_size, max_value=max_size, value=default_size)
location = st.selectbox("📍 Location", locations)
house_type = st.selectbox("🏠 House Type", house_types)

# --- Prepare DataFrame for Prediction ---
input_df = pd.DataFrame([{
    "house_size_in_sqft": house_size,
    "location": location,
    "house_type": house_type
}])

# --- Make Prediction ---
prediction = model.predict(input_df)[0]
st.success(f"💰 Predicted Rental Price: ${round(prediction, 2)}")
