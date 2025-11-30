import streamlit as st
import sys
import os
import math

# Page configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="AgriIntel Pro - Advanced Agricultural Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add path for custom components
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.styles import load_css
from components.sidebar import show_sidebar

# Load CSS
load_css()

# Sidebar
show_sidebar()

# Enhanced CSS Styling
st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Hero section styling */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 0 0 30px 30px;
        color: white;
        margin: -2rem -2rem 2rem -2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FFD700, #FFFFFF, #98FB98);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        opacity: 0.9;
        margin-bottom: 2rem;
    }
    
    /* Feature cards styling */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #4CAF50;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        margin-bottom: 1rem;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        color: #4CAF50;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        color: #2E8B57;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
    }
    
    /* Metric styling */
    .stMetric {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        text-align: center;
    }
    
    /* Testimonial styling */
    .testimonial-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
        height: 100%;
    }
    
    .testimonial-text {
        color: #555;
        font-style: italic;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .testimonial-author {
        color: #2E8B57;
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    
    .testimonial-role {
        color: #888;
        font-size: 0.9rem;
    }
    
    /* CTA section styling */
    .cta-section {
        background: linear-gradient(135deg, #2E8B57 0%, #228B22 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }
    
    .cta-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 2rem;
    }
    
    /* Crop cards styling */
    .crop-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        height: 100%;
    }
    
    .crop-card:hover {
        border-color: #4CAF50;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.2);
    }
    
    .crop-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .crop-name {
        font-weight: 600;
        color: #2E8B57;
        font-size: 0.9rem;
    }
    
    /* Supported crops section */
    .crops-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #666;
        padding: 2rem 1rem;
        margin-top: 3rem;
        border-top: 1px solid #e0e0e0;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
        }
        
        .feature-card {
            margin-bottom: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-container">
    <div style="text-align: center;">
        <h1 class="hero-title">🌱 AgriIntel Pro</h1>
        <p class="hero-subtitle">Artificial intelligence for modern agriculture</p>
        <p style="font-size: 1.1rem; opacity: 0.9; max-width: 600px; margin: 0 auto;">
            Optimize your yields, reduce your costs and make informed decisions with our advanced agricultural analysis platform.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero stats
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Prediction Accuracy", "+95%", "AI-Powered")

with col2:
    st.metric("Crops Analyzed", "50+", "Comprehensive")

with col3:
    st.metric("Intelligent Support", "24/7", "Always Available")

with col4:
    st.metric("Satisfied Farmers", "1000+", "Trusted Results")

st.markdown("---")

# ==================== FEATURES SECTION ====================
st.header(" Our Smart Solutions")
st.subheader("Discover how our technology is revolutionizing modern agriculture")

# Create three columns for features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon"></div>
        <h3 class="feature-title">Smart Prediction</h3>
        <p class="feature-description">
            Our AI analyzes your specific conditions to recommend the optimal crop 
            with 95% accuracy. Maximize your yields with data-driven decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Try Now", key="prediction_btn"):
        st.switch_page("pages/Crop_Prediction.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon"></div>
        <h3 class="feature-title">Advanced Soil Analysis</h3>
        <p class="feature-description">
            Comprehensive soil evaluation with personalized improvement recommendations. 
            Optimize your nutrient inputs and reduce fertilizer costs.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Analyze My Soil", key="soil_btn"):
        st.switch_page("pages/Soil_Analysis.py")

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon"></div>
        <h3 class="feature-title">Expert Crop Guide</h3>
        <p class="feature-description">
            Access a comprehensive knowledge base on ideal conditions for each crop. 
            Become an expert in agricultural management.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Consult Guide", key="guide_btn"):
        st.switch_page("pages/Crop_Guide.py")

st.markdown("---")

# ==================== STATS SECTION ====================
st.header("Proven Results")
st.subheader("See the impact our platform has made for farmers worldwide")

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric("Average Yield Increase", "+30%", "Higher Production")

with stats_col2:
    st.metric("Operating Cost Reduction", "-25%", "More Savings")

with stats_col3:
    st.metric("Resource Efficiency", "+40%", "Better Usage")

with stats_col4:
    st.metric("Decision Time", "-60%", "Faster Choices")

st.markdown("---")

# ==================== SUPPORTED CROPS SECTION ====================
st.header(" Supported Crops")
st.subheader("Comprehensive coverage of major agricultural crops")

# Mapping crop names to emoji icons
CROP_ICONS = {
    "apple": "🍎",
    "banana": "🍌",
    "blackgram": "🫘",
    "chickpea": "🥙",
    "coconut": "🥥",
    "coffee": "☕",
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
    "papaya": "🍈",
    "pigeonpeas": "🌱",
    "pomegranate": "🍎",
    "rice": "🍚",
    "watermelon": "🍉"
}

# Sample crops data (you can replace this with your actual data)
crops = [
    "apple", "banana", "blackgram", "chickpea", "coconut", 
    "coffee", "cotton", "grapes", "jute", "kidneybeans", 
    "lentil", "maize", "mango", "mothbeans", "mungbean", 
    "muskmelon", "orange", "papaya", "pigeonpeas", "pomegranate", 
    "rice", "watermelon"
]

# Display crops in a grid layout
cols = 6  # Number of columns in the grid
rows = math.ceil(len(crops) / cols)

st.markdown('<div class="crops-section">', unsafe_allow_html=True)

for i in range(rows):
    col_list = st.columns(cols)
    for j in range(cols):
        idx = i * cols + j
        if idx < len(crops):
            crop = crops[idx]
            icon = CROP_ICONS.get(crop, "🌱")  # fallback icon
            with col_list[j]:
                st.markdown(f"""
                <div class="crop-card">
                    <div class="crop-icon">{icon}</div>
                    <div class="crop-name">{crop.capitalize()}</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ==================== TESTIMONIALS ====================
st.header(" Trusted By Farmers")
st.subheader("Discover testimonials from our partner farmers")

test_col1, test_col2, test_col3 = st.columns(3)

with test_col1:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">
            "This platform has revolutionized my decision-making process. 
            My yields increased by 35% in just one season thanks to the 
            AI's personalized recommendations."
        </p>
        <p class="testimonial-author">Pierre Martin</p>
        <p class="testimonial-role">Cereal Farmer in Burgundy</p>
    </div>
    """, unsafe_allow_html=True)

with test_col2:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">
            "The precise soil analysis allowed me to optimize my fertilizer 
            inputs and make significant savings. An essential tool for every 
            modern farmer."
        </p>
        <p class="testimonial-author">Marie Dubois</p>
        <p class="testimonial-role">Winegrower in Provence</p>
    </div>
    """, unsafe_allow_html=True)

with test_col3:
    st.markdown("""
    <div class="testimonial-card">
        <p class="testimonial-text">
            "The interface is intuitive and the results are remarkable. 
            I reduced my production costs by 20% while improving the 
            quality of my harvests."
        </p>
        <p class="testimonial-author">Jean Leroy</p>
        <p class="testimonial-role">Market Gardener in Normandy</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== CTA SECTION ====================
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Transform Your Farm?</h2>
    <p class="cta-subtitle">
        Join thousands of farmers already using our artificial intelligence 
        to optimize their yields and maximize their profits.
    </p>
</div>
""", unsafe_allow_html=True)

cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    if st.button(" Start Free Analysis", use_container_width=True, key="cta1"):
        st.switch_page("pages/Crop_Prediction.py")

with cta_col2:
    if st.button(" Discover Our Solutions", use_container_width=True, key="cta2"):
        st.switch_page("pages/Crop_Guide.py")

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <div style="margin-bottom: 1rem;">
        <a href="#" style="color: #4CAF50; text-decoration: none; margin: 0 1rem;">Legal Notice</a>
        <a href="#" style="color: #4CAF50; text-decoration: none; margin: 0 1rem;">Privacy</a>
        <a href="#" style="color: #4CAF50; text-decoration: none; margin: 0 1rem;">Contact</a>
        <a href="#" style="color: #4CAF50; text-decoration: none; margin: 0 1rem;">Support</a>
    </div>
    <p style="margin: 0; font-size: 0.9rem;">
        © 2024 AgriIntel Pro. All rights reserved. | Designed for tomorrow's agriculture ❤️
    </p>
</div>
""", unsafe_allow_html=True)