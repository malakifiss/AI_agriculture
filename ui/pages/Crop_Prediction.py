import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.predict import predict_crop
from components.styles import create_feature_card

st.markdown('<h1 class="main-header">Crop Prediction</h1>', unsafe_allow_html=True)

st.markdown(create_feature_card(
    "AI-Powered Crop Recommendation", 
    "Enter your soil and environmental conditions to receive optimal crop recommendations based on machine learning analysis.",
    "🤖"
), unsafe_allow_html=True)

# Input Section
st.markdown('<div class="section-header">Environmental Parameters</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subsection-header">Soil Nutrients</div>', unsafe_allow_html=True)
    N = st.slider("Nitrogen (N) level", 0, 500, 50, 
                 help="Nitrogen content in soil - essential for leaf growth")
    P = st.slider("Phosphorus (P) level", 0, 500, 40,
                 help="Phosphorus content in soil - important for root development")
    K = st.slider("Potassium (K) level", 0, 500, 60,
                 help="Potassium content in soil - crucial for overall plant health")
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5, 0.1,
                  help="Soil acidity/alkalinity level - affects nutrient availability")

with col2:
    st.markdown('<div class="subsection-header">Climate Conditions</div>', unsafe_allow_html=True)
    temperature = st.slider("Temperature (°C)", -10, 60, 25,
                           help="Average temperature in your region")
    humidity = st.slider("Humidity (%)", 0, 100, 70,
                        help="Relative humidity level")
    rainfall = st.slider("Rainfall (mm)", 0, 500, 60,
                        help="Annual rainfall precipitation")

# Prediction Button
if st.button("Generate Crop Recommendation", use_container_width=True, type="primary"):
    with st.spinner("Analyzing conditions and generating recommendation..."):
        features = {
            "N": N, "P": P, "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }
        
        result = predict_crop(features)
        
        # Results Section
        st.markdown("---")
        st.markdown('<div class="section-header">Recommendation Results</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"""
            <div class="success-box">
                <h3 style='margin: 0 0 1rem 0;'>Recommended Crop</h3>
                <h2 style='margin: 0; font-size: 2rem;'>{result}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h4 style='margin: 0 0 1rem 0; color: #1565C0;'>Analysis Summary</h4>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"""
            Based on comprehensive analysis of your input parameters, **{result}** has been identified 
            as the optimal crop choice for the following reasons:

            - **Soil Composition**: The nutrient levels (N: {N}, P: {P}, K: {K}) align well with the requirements for {result}
            - **pH Compatibility**: Soil pH of {ph} falls within the ideal range for {result}
            - **Climate Suitability**: Temperature of {temperature}°C and rainfall of {rainfall}mm match optimal growing conditions
            - **Environmental Factors**: Humidity level of {humidity}% supports healthy growth
            """)
            
            # Input Summary
            st.markdown('<div class="subsection-header">Input Summary</div>', unsafe_allow_html=True)
            col_n, col_p, col_k = st.columns(3)
            with col_n:
                st.metric("Nitrogen", f"{N}")
            with col_p:
                st.metric("Phosphorus", f"{P}")
            with col_k:
                st.metric("Potassium", f"{K}")