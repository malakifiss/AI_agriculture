import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_crop_yield

st.title("🌾 Crop Yield Prediction")

st.write("Enter agriculture parameters below:")

nitrogen = st.number_input("Nitrogen (N)", 0, 500)
phosphorus = st.number_input("Phosphorus (P)", 0, 500)
potassium = st.number_input("Potassium (K)", 0, 500)
temperature = st.number_input("Temperature (°C)", -10, 60)
humidity = st.number_input("Humidity (%)", 0, 100)
ph = st.number_input("Soil pH", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0, 1000)

if st.button("Predict Yield"):
    input_data = {
        "N": nitrogen,
        "P": phosphorus,
        "K": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    result = predict_crop_yield(input_data)
    st.success(f"🌿 Estimated Crop Yield: **{result:.2f} units**")
