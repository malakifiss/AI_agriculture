import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from components.styles import create_progress_bar, create_feature_card

# Page Config
st.set_page_config(
    page_title="Soil Quality Analysis",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load Font Awesome
st.markdown("""
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-header">
    <i class="fa-solid fa-seedling" 
       style="color: #2E8B57; margin-right: 10px;"></i>
    Soil Quality Analysis
</h1>
""", unsafe_allow_html=True)



# Input Section
st.markdown('<div class="section-header">Soil Parameter Input</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-flask"></i> Nutrient Levels</div>', unsafe_allow_html=True)
    N = st.slider("Nitrogen Level (N)", 0, 500, 50, help="Essential for leaf and stem growth")
    P = st.slider("Phosphorus Level (P)", 0, 500, 40, help="Critical for root development and flowering")
    K = st.slider("Potassium Level (K)", 0, 500, 60, help="Important for overall plant health")
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.5, 0.1, help="Measures soil acidity/alkalinity")

with col2:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-chart-line"></i> Analysis Results</div>', unsafe_allow_html=True)
    
    nutrient_score = (N + P + K) / 15
    ph_score = max(0, 100 - abs(ph - 6.5) * 20)
    soil_score = min(100, (nutrient_score + ph_score) / 2)

    st.markdown(f"### Soil Quality Score: {soil_score:.1f}/100")
    
    if soil_score >= 80:
        st.success("**Excellent** - Soil conditions are optimal for most crops")
    elif soil_score >= 60:
        st.warning("**Good** - Soil conditions are adequate")
    else:
        st.error("**Needs Improvement** - Soil amendments recommended")

    st.markdown(create_progress_bar(soil_score, 100), unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><i class="fa-solid fa-leaf"></i> Nutrient Analysis</div>', unsafe_allow_html=True)
    st.markdown(create_progress_bar(N, 200), unsafe_allow_html=True)
    st.markdown(create_progress_bar(P, 150), unsafe_allow_html=True)
    st.markdown(create_progress_bar(K, 200), unsafe_allow_html=True)

# Recommendations Section
st.markdown("---")
st.markdown('<div class="section-header"><i class="fa-solid fa-circle-info"></i> Improvement Recommendations</div>', unsafe_allow_html=True)

rec_col1, rec_col2 = st.columns(2)

with rec_col1:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-vial"></i> Soil pH Management</div>', unsafe_allow_html=True)
    if ph < 6.0:
        st.error("""
        **Soil is too acidic**
        - Apply agricultural lime
        - Target pH: 6.0–7.0
        """)
    elif ph > 7.5:
        st.error("""
        **Soil is too alkaline**
        - Apply elemental sulfur
        - Add organic matter
        """)
    else:
        st.success("""
        **Optimal pH Range**
        - Current pH suitable for most crops
        """)
    
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-droplet"></i> Nitrogen Management</div>', unsafe_allow_html=True)
    if N < 30:
        st.warning("""
        **Nitrogen Deficiency**
        - Apply nitrogen-rich fertilizers
        """)
    else:
        st.success("""
        **Adequate Nitrogen**
        - Maintain current levels
        """)

with rec_col2:
    st.markdown('<div class="subsection-header"><i class="fa-solid fa-seedling"></i> Phosphorus Management</div>', unsafe_allow_html=True)
    if P < 20:
        st.warning("""
        **Low Phosphorus**
        - Apply bone meal or superphosphate
        """)
    else:
        st.success("""
        **Phosphorus Levels Good**
        """)

    st.markdown('<div class="subsection-header"><i class="fa-solid fa-bolt"></i> Potassium Management</div>', unsafe_allow_html=True)
    if K < 40:
        st.warning("""
        **Low Potassium**
        - Apply potash or wood ash
        """)
    else:
        st.success("""
        **Potassium Levels Optimal**
        """)
