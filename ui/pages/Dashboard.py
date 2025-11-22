import streamlit as st
import pandas as pd
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from components.styles import create_metric_card, create_feature_card

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/crop_yield.csv")

df = load_data()

# Page content
st.markdown('<h1 class="main-header">Agriculture AI Assistant</h1>', unsafe_allow_html=True)

# Introduction
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <p style='color: #666; font-size: 1.1rem; line-height: 1.6;'>
        Advanced agricultural intelligence platform providing data-driven insights 
        for optimal crop selection and soil management.
    </p>
</div>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown('<div class="section-header">Core Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_feature_card(
        "Crop Prediction", 
        "AI-powered recommendations for optimal crop selection based on soil and climate conditions.",
        "🌿"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_feature_card(
        "Growing Guide", 
        "Comprehensive information on ideal conditions and requirements for various crops.",
        "📊"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_feature_card(
        "Soil Analysis", 
        "Detailed soil quality assessment and improvement recommendations.",
        "🧪"
    ), unsafe_allow_html=True)

# Quick Stats
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

# Crop Distribution
st.markdown('<div class="section-header">Crop Distribution</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    crop_counts = df["label"].value_counts()
    st.bar_chart(crop_counts)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4 style='margin: 0 0 0.5rem 0; color: #1565C0;'>Dataset Overview</h4>
        <p style='margin: 0; color: #455A64;'>
            The dataset contains information on various crops with detailed 
            environmental and soil parameter measurements.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Supported Crops
st.markdown('<div class="section-header">Supported Crops</div>', unsafe_allow_html=True)

crops = sorted(df["label"].unique())
cols = 4
rows = math.ceil(len(crops) / cols)

for i in range(rows):
    col_list = st.columns(cols)
    for j in range(cols):
        idx = i * cols + j
        if idx < len(crops):
            with col_list[j]:
                st.info(crops[idx])

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem; font-size: 0.9rem;'>
    <p>Agriculture AI Assistant • Data-Driven Farming Solutions</p>
</div>
""", unsafe_allow_html=True)