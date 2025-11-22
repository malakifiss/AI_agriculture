import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_crop
import pandas as pd

# Load dataset to extract ideal conditions
df = pd.read_csv("data/crop_yield.csv")

st.sidebar.title("🌾 Agriculture AI")
page = st.sidebar.radio("Choose an option", [
    "Predict Best Crop",
    "Best Conditions for a Crop"
])

# ---------------------- PAGE 1 -------------------------
if page == "Predict Best Crop":
    st.title("🌿 Predict the Best Vegetable to Plant")

    N = st.number_input("Nitrogen (N)", 0, 500)
    P = st.number_input("Phosphorus (P)", 0, 500)
    K = st.number_input("Potassium (K)", 0, 500)
    temperature = st.number_input("Temperature (°C)", -10, 60)
    humidity = st.number_input("Humidity (%)", 0, 100)
    ph = st.number_input("Soil pH", 0.0, 14.0)
    rainfall = st.number_input("Rainfall (mm)", 0, 500)

    if st.button("Predict Crop"):
        features = {
            "N": N, "P": P, "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }

        result = predict_crop(features)
        st.success(f"🌱 Recommended Crop: **{result}**")


# ---------------------- PAGE 2 -------------------------
elif page == "Best Conditions for a Crop":
    st.title("🌤️ Best Conditions for Each Vegetable")

    crops = sorted(df["label"].unique())
    selected_crop = st.selectbox("Select a crop:", crops)

    crop_data = df[df["label"] == selected_crop]

    ideal = crop_data.mean(numeric_only=True)

    st.subheader(f"🌱 Ideal Conditions for **{selected_crop}**")
    st.write(f"**Nitrogen (N):** {ideal['N']:.1f}")
    st.write(f"**Phosphorus (P):** {ideal['P']:.1f}")
    st.write(f"**Potassium (K):** {ideal['K']:.1f}")
    st.write(f"**Temperature:** {ideal['temperature']:.1f}°C")
    st.write(f"**Humidity:** {ideal['humidity']:.1f}%")
    st.write(f"**Soil pH:** {ideal['ph']:.1f}")
    st.write(f"**Rainfall:** {ideal['rainfall']:.1f} mm")
