import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components.styles import create_progress_bar, create_feature_card

# Page config
st.set_page_config(
    page_title="Soil Quality Analysis",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Font Awesome
st.markdown("""
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
    .main-title {
        font-size: 45px;
        font-weight: 900;
        color: #2E8B57;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 26px;
        font-weight: 700;
        margin-top: 30px;
        color: #1f4f34;
        padding-bottom: 10px;
        border-bottom: 3px solid #2E8B57;
    }
    .sub-header {
        font-size: 19px;
        font-weight: 600;
        margin: 20px 0 10px;
        color: #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title"><i class="fa-solid fa-seedling"></i> Soil Quality Analysis</div>',
            unsafe_allow_html=True)

# Inputs
st.markdown('<div class="section-header"><i class="fa-solid fa-sliders"></i> Soil Parameter Input</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="sub-header"><i class="fa-solid fa-flask"></i> Nutrient Levels</div>', unsafe_allow_html=True)
    N = st.slider("Nitrogen (N)", 0, 500, 50)
    P = st.slider("Phosphorus (P)", 0, 500, 40)
    K = st.slider("Potassium (K)", 0, 500, 60)
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.5, 0.1)

with col2:
    st.markdown('<div class="sub-header"><i class="fa-solid fa-chart-line"></i> Analysis Results</div>', unsafe_allow_html=True)

    nutrient_score = (N + P + K) / 15
    ph_score = max(0, 100 - abs(ph - 6.5) * 20)
    soil_score = min(100, (nutrient_score + ph_score) / 2)

    st.markdown(f"###  Soil Quality Score: **{soil_score:.1f}/100**")
    st.markdown(create_progress_bar(soil_score, 100), unsafe_allow_html=True)

    if soil_score >= 80:
        st.success("Excellent — Soil conditions are ideal ")
    elif soil_score >= 60:
        st.warning("Good — Soil is suitable but could be improved ")
    else:
        st.error("Needs Improvement — Soil amendments recommended ")

    # Nutrient progress bars
    st.markdown('<div class="sub-header"><i class="fa-solid fa-leaf"></i> Nutrient Breakdown</div>', unsafe_allow_html=True)
    st.markdown(create_progress_bar(N, 200), unsafe_allow_html=True)
    st.markdown(create_progress_bar(P, 150), unsafe_allow_html=True)
    st.markdown(create_progress_bar(K, 200), unsafe_allow_html=True)

# Recommendations
st.markdown('<div class="section-header"><i class="fa-solid fa-bulb"></i> Recommendations</div>', unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="sub-header"><i class="fa-solid fa-droplet"></i> Soil pH</div>', unsafe_allow_html=True)
    if ph < 6.0:
        st.error("Too acidic — Consider adding lime")
    elif ph > 7.5:
        st.error("Too alkaline — Apply organic matter or sulfur")
    else:
        st.success("Ideal pH range ")

    st.markdown('<div class="sub-header"><i class="fa-solid fa-bottle-droplet"></i> Nitrogen</div>', unsafe_allow_html=True)
    if N < 30:
        st.warning("Low Nitrogen — Use nitrogen-rich fertilizer")
    else:
        st.success("Nitrogen levels sufficient ")

with colB:
    st.markdown('<div class="sub-header"><i class="fa-solid fa-seedling"></i> Phosphorus</div>', unsafe_allow_html=True)
    if P < 20:
        st.warning("Low Phosphorus — Consider bone meal / phosphate fertilizer")
    else:
        st.success("Phosphorus levels are good ")

    st.markdown('<div class="sub-header"><i class="fa-solid fa-bolt"></i> Potassium</div>', unsafe_allow_html=True)
    if K < 40:
        st.warning("Low Potassium — Apply potash or compost")
    else:
        st.success("Potassium levels ideal ")
