import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from components.styles import create_progress_bar, create_feature_card

st.markdown('<h1 class="main-header">Soil Quality Analysis</h1>', unsafe_allow_html=True)

st.markdown(create_feature_card(
    "Comprehensive Soil Assessment", 
    "Detailed analysis of soil parameters with improvement recommendations for optimal crop growth.",
    "🔍"
), unsafe_allow_html=True)

# Input Section
st.markdown('<div class="section-header">Soil Parameter Input</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="subsection-header">Nutrient Levels</div>', unsafe_allow_html=True)
    N = st.slider("Nitrogen Level (N)", 0, 500, 50, 
                 help="Essential for leaf and stem growth")
    P = st.slider("Phosphorus Level (P)", 0, 500, 40,
                 help="Critical for root development and flowering")
    K = st.slider("Potassium Level (K)", 0, 500, 60,
                 help="Important for overall plant health and disease resistance")
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.5, 0.1,
                  help="Measures soil acidity/alkalinity - affects nutrient availability")

with col2:
    st.markdown('<div class="subsection-header">Analysis Results</div>', unsafe_allow_html=True)
    
    # Calculate soil quality score
    nutrient_score = (N + P + K) / 15
    ph_score = max(0, 100 - abs(ph - 6.5) * 20)
    soil_score = min(100, (nutrient_score + ph_score) / 2)
    
    # Quality Assessment
    st.markdown(f"### Soil Quality Score: {soil_score:.1f}/100")
    
    if soil_score >= 80:
        st.success("**Excellent** - Soil conditions are optimal for most crops")
    elif soil_score >= 60:
        st.warning("**Good** - Soil conditions are adequate with minor improvements possible")
    else:
        st.error("**Needs Improvement** - Significant soil amendments recommended")
    
    # Progress visualization
    st.markdown(create_progress_bar(soil_score, 100), unsafe_allow_html=True)
    
    # Nutrient Analysis
    st.markdown('<div class="subsection-header">Nutrient Analysis</div>', unsafe_allow_html=True)
    st.markdown(create_progress_bar(N, 200), unsafe_allow_html=True)
    st.markdown(create_progress_bar(P, 150), unsafe_allow_html=True)
    st.markdown(create_progress_bar(K, 200), unsafe_allow_html=True)

# Recommendations Section
st.markdown("---")
st.markdown('<div class="section-header">Improvement Recommendations</div>', unsafe_allow_html=True)

rec_col1, rec_col2 = st.columns(2)

with rec_col1:
    # pH Recommendations
    st.markdown('<div class="subsection-header">Soil pH Management</div>', unsafe_allow_html=True)
    if ph < 6.0:
        st.error("""
        **Soil is too acidic**
        - Apply agricultural lime to raise pH
        - Target pH range: 6.0-7.0
        - Test soil after 3-6 months
        """)
    elif ph > 7.5:
        st.error("""
        **Soil is too alkaline**
        - Apply elemental sulfur to lower pH
        - Incorporate organic matter
        - Consider acidifying fertilizers
        """)
    else:
        st.success("""
        **Optimal pH Range**
        - Current pH is suitable for most crops
        - Maintain current levels
        - Regular monitoring recommended
        """)
    
    # Nitrogen Recommendations
    st.markdown('<div class="subsection-header">Nitrogen Management</div>', unsafe_allow_html=True)
    if N < 30:
        st.warning("""
        **Nitrogen Deficiency**
        - Apply nitrogen-rich fertilizers
        - Options: Urea, Ammonium Nitrate
        - Consider organic sources: compost, manure
        """)
    else:
        st.success("""
        **Adequate Nitrogen Levels**
        - Current levels support healthy growth
        - Maintain balanced application
        - Monitor plant response
        """)

with rec_col2:
    # Phosphorus Recommendations
    st.markdown('<div class="subsection-header">Phosphorus Management</div>', unsafe_allow_html=True)
    if P < 20:
        st.warning("""
        **Phosphorus Deficiency**
        - Apply phosphorus fertilizers
        - Options: Superphosphate, Bone Meal
        - Improve with rock phosphate
        """)
    else:
        st.success("""
        **Adequate Phosphorus Levels**
        - Sufficient for root development
        - Maintain current application rates
        - Monitor soil levels annually
        """)
    
    # Potassium Recommendations
    st.markdown('<div class="subsection-header">Potassium Management</div>', unsafe_allow_html=True)
    if K < 40:
        st.warning("""
        **Potassium Deficiency**
        - Apply potassium fertilizers
        - Options: Muriate of Potash
        - Organic option: Wood Ash
        """)
    else:
        st.success("""
        **Adequate Potassium Levels**
        - Supports plant health and resistance
        - Maintain balanced nutrition
        - Regular soil testing recommended
        """)