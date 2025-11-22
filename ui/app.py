import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.predict import predict_crop

st.title("🥕 Multi-Crop Prediction System")

st.write("Enter your soil and climate information:")

N = st.number_input("Nitrogen (N)", 0, 500)
P = st.number_input("Phosphorus (P)", 0, 500)
K = st.number_input("Potassium (K)", 0, 500)
temperature = st.number_input("Temperature (°C)", -10, 60)
humidity = st.number_input("Humidity (%)", 0, 100)
ph = st.number_input("Soil pH", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0, 500)

if st.button("Predict Best Crop"):
    data = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    crop = predict_crop(data)
    st.success(f"🌱 Recommended Crop: **{crop.capitalize()}**")
