import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.predict import predict_crop
from components.styles import create_feature_card

# Page Config
st.set_page_config(
    page_title="Crop Prediction",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Font Awesome + Custom CSS
st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
.title {
    font-size: 45px;
    font-weight: 900;
    color: #2E8B57;
    margin-bottom: 15px;
}
.section-header {
    font-size: 24px;
    margin-top: 25px;
    padding-bottom: 8px;
    font-weight: 700;
    border-bottom: 3px solid #2E8B57;
    color: #114d32;
}
.subsection-header {
    font-size: 18px;
    font-weight: 600;
    margin: 15px 0 10px;
    color: #227a4f;
}
.results-card {
    background: #e9f7ef;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border-left: 6px solid #2E8B57;
}
.summary-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title"><i class="fa-solid fa-seedling"></i> Crop Recommendation</div>',
            unsafe_allow_html=True)

st.markdown(create_feature_card(
    "AI-Powered Crop Recommendation",
    "Provide environmental and soil details to get a smart crop suggestion 🌱",
    "<i class='fa-solid fa-brain'></i>"
), unsafe_allow_html=True)

# =======================================================================================
# Inputs
# =======================================================================================
st.markdown('<div class="section-header"><i class="fa-solid fa-sliders"></i> Environmental Parameters</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-flask"></i> Soil Nutrients</div>',
                unsafe_allow_html=True)
    N = st.slider("Nitrogen (N)", 0, 500, 50)
    P = st.slider("Phosphorus (P)", 0, 500, 40)
    K = st.slider("Potassium (K)", 0, 500, 60)
    ph = st.slider("Soil pH", 0.0, 14.0, 6.5, 0.1)

with col2:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-cloud-sun"></i> Climate Conditions</div>',
                unsafe_allow_html=True)
    temperature = st.slider("Temperature (°C)", -10, 60, 25)
    humidity = st.slider("Humidity (%)", 0, 100, 70)
    rainfall = st.slider("Rainfall (mm)", 0, 500, 60)

# Button
submit = st.button(" Generate Recommendation", use_container_width=True)

# =======================================================================================
# Prediction Results
# =======================================================================================
if submit:
    with st.spinner(" Analyzing environment..."):
        features = {
            "N": N, "P": P, "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }

        result = predict_crop(features)

        st.markdown("---")
        st.markdown(
            '<div class="section-header"><i class="fa-solid fa-seedling"></i> Recommendation Results</div>',
            unsafe_allow_html=True
        )

        colA, colB = st.columns([1, 2])

        with colA:
            st.markdown(f"""
            <div class="results-card">
                <h4 style="margin:0;">Recommended Crop</h4>
                <h2 style="margin:10px 0; font-size:2rem;"> {result}</h2>
            </div>
            """, unsafe_allow_html=True)

        with colB:
            st.markdown('<div class="summary-box">', unsafe_allow_html=True)
            st.write(f"""
###  Why **{result}**?
The environmental and soil conditions align strongly with the growing
requirements of **{result}**:

- **Nitrogen:** {N}
- **Phosphorus:** {P}
- **Potassium:** {K}
- **Soil pH:** {ph}
- **Temperature:** {temperature}°C
- **Humidity:** {humidity}%
- **Rainfall:** {rainfall} mm
""")
            st.markdown('</div>', unsafe_allow_html=True)


# =======================================================================================
# Input Summary (bottom)
# =======================================================================================
if submit:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-receipt"></i> Input Summary</div>',
                unsafe_allow_html=True)

    i_col1, i_col2, i_col3 = st.columns(3)
    i_col1.metric("Nitrogen", N)
    i_col2.metric("Phosphorus", P)
    i_col3.metric("Potassium", K)
