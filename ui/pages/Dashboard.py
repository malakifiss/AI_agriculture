import streamlit as st
import pandas as pd
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from components.styles import create_metric_card, create_feature_card
# Page Config
st.set_page_config(
    page_title="Fruits and Vegetables Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load Font Awesome
st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/crop_yield.csv")

df = load_data()

# PAGE TITLE WITH ICON
st.markdown("""
<h1 class="main-header">
    <i class="fa-solid fa-leaf" style="color:#2E8B57;"></i> 
    Agriculture AI Assistant
</h1>
""", unsafe_allow_html=True)

# INTRODUCTION
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <p style='color: #666; font-size: 1.1rem; line-height: 1.6;'>
        Advanced agricultural intelligence platform providing data-driven insights 
        for optimal crop selection, soil management, and growing recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

# FEATURE CARDS
st.markdown('<div class="section-header">Core Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_feature_card(
        "<i class='fa-solid fa-seedling' style='margin-right:8px;'></i> Crop Prediction", 
        "AI-powered recommendations for choosing the right crop.",
        None  # No icon on top
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_feature_card(
        "<i class='fa-solid fa-book-open' style='margin-right:8px;'></i> Growing Guide", 
        "Ideal conditions & growing requirements for each crop.",
        None
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_feature_card(
        "<i class='fa-solid fa-vial' style='margin-right:8px;'></i> Soil Analysis", 
        "Detailed evaluation of soil nutrients & pH balance.",
        None
    ), unsafe_allow_html=True)


# QUICK STATS
st.markdown('<div class="section-header">Agricultural Insights</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_crops = len(df["label"].unique())
    st.markdown(create_metric_card(total_crops, "Crop Types"), unsafe_allow_html=True)

with col2:
    avg_temp = df["temperature"].mean()
    st.markdown(create_metric_card(f"{avg_temp:.1f}°C", "Avg Temperature"), unsafe_allow_html=True)

with col3:
    avg_rainfall = df["rainfall"].mean()
    st.markdown(create_metric_card(f"{avg_rainfall:.1f}mm", "Avg Rainfall"), unsafe_allow_html=True)

with col4:
    avg_ph = df["ph"].mean()
    st.markdown(create_metric_card(f"{avg_ph:.1f}", "Avg Soil pH"), unsafe_allow_html=True)

# CROP DISTRIBUTION
st.markdown('<div class="section-header">Crop Distribution</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    crop_counts = df["label"].value_counts()
    st.bar_chart(crop_counts)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4 style='margin: 0 0 0.5rem 0; color: #1565C0;'>
            <i class="fa-solid fa-circle-info"></i> Dataset Overview
        </h4>
        <p style='margin: 0; color: #455A64;'>
            This dataset contains soil nutrients, climate conditions, and
            crop labels used to train the prediction model.
        </p>
    </div>
    """, unsafe_allow_html=True)


# Mapping crop names to Font Awesome icons
CROP_ICONS = {
    "apple": "🍎",
    "banana": "🍌",
    "blackgram": "🫘",
    "chickpea": "🥙",
    "coconut": "🥥",
    "coffee": "🌰",
    "cotton": "🧵",
    "grapes": "🍇",
    "jute": "🪢",
    "kidneybeans": "🫘",
    "lentil": "🥣",
    "maize": "🌽",
    "mango": "🥭",
    "mothbeans": "🫘",
    "mungbean": "🫘",
    "muskmelon": "🍈",
    "orange": "🍊",
    "papaya": "🟠",
    "pigeonpeas": "🌱",
    "pomegranate": "🍎",
    "rice": "🍚",
    "watermelon": "🍉"
}

# SUPPORTED CROPS
st.markdown('<div class="section-header">Supported Crops</div>', unsafe_allow_html=True)

crops = sorted(df["label"].unique())
cols = 4
rows = math.ceil(len(crops) / cols)

for i in range(rows):
    col_list = st.columns(cols)
    for j in range(cols):
        idx = i * cols + j
        if idx < len(crops):
            crop = crops[idx]
            icon = CROP_ICONS.get(crop, "🌱")  # fallback icon
            with col_list[j]:
                st.info(f"{icon} {crop.capitalize()}")

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem; font-size: 0.9rem;'>
    <p>Agriculture AI Assistant • Smart Farming Solutions</p>
</div>
""", unsafe_allow_html=True)
