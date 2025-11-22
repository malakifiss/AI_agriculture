import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/crop_yield.csv")

df = load_data()

st.markdown('<h1 class="main-header">Crop Growing Guide</h1>', unsafe_allow_html=True)

st.markdown("""
<div style='margin-bottom: 2rem;'>
    <p style='color: #666; line-height: 1.6;'>
        Comprehensive reference guide containing optimal growing conditions and requirements 
        for various agricultural crops based on extensive data analysis.
    </p>
</div>
""", unsafe_allow_html=True)

crops = sorted(df["label"].unique())
selected_crop = st.selectbox("Select Crop", crops, 
                           help="Choose a crop to view detailed growing information")

if selected_crop:
    crop_data = df[df["label"] == selected_crop]
    ideal = crop_data.mean(numeric_only=True)
    
    st.markdown("---")
    
    # Crop Information
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f'<div class="section-header">{selected_crop} - Growing Conditions</div>', unsafe_allow_html=True)
        
        # Optimal Ranges
        st.markdown('<div class="subsection-header">Optimal Parameter Ranges</div>', unsafe_allow_html=True)
        
        metrics_col1, metrics_col2 = st.columns(2)
        
        with metrics_col1:
            st.metric("Temperature", f"{ideal['temperature']:.1f}°C")
            st.metric("Humidity", f"{ideal['humidity']:.1f}%")
            st.metric("Nitrogen (N)", f"{ideal['N']:.1f}")
        
        with metrics_col2:
            st.metric("Soil pH", f"{ideal['ph']:.1f}")
            st.metric("Phosphorus (P)", f"{ideal['P']:.1f}")
            st.metric("Potassium (K)", f"{ideal['K']:.1f}")
        
        st.metric("Rainfall", f"{ideal['rainfall']:.1f} mm")
    
    with col2:
        st.markdown('<div class="subsection-header">Crop Statistics</div>', unsafe_allow_html=True)
        
        # Display statistics
        st.metric("Data Samples", len(crop_data))
        
        # Value Ranges
        st.markdown("**Parameter Ranges:**")
        for col in ['temperature', 'humidity', 'ph']:
            min_val = crop_data[col].min()
            max_val = crop_data[col].max()
            st.write(f"**{col.title()}**: {min_val:.1f} - {max_val:.1f}")
        
        # Growing Recommendations
        st.markdown('<div class="subsection-header">Growing Recommendations</div>', unsafe_allow_html=True)
        
        if selected_crop.lower() in ['rice', 'wheat']:
            st.info("""
            **Key Requirements:**
            - Consistent water supply essential
            - Prefers warm growing temperatures
            - Well-drained soil conditions
            - Regular nutrient monitoring
            """)
        elif selected_crop.lower() in ['maize', 'corn']:
            st.info("""
            **Key Requirements:**
            - Plant in warm soil conditions
            - Requires full sunlight exposure
            - Regular irrigation important
            - Soil fertility management
            """)
        else:
            st.info("""
            **General Guidelines:**
            - Monitor soil moisture levels
            - Regular soil testing recommended
            - Adjust pH as necessary
            - Balanced nutrient application
            """)