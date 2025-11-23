import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components.styles import load_css
from components.sidebar import show_sidebar
st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)
# Load CSS
load_css()

# Page Config
st.set_page_config(
    page_title="Agriculture AI Assistant",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
show_sidebar()

# Welcome Section
st.markdown("""
<div style='text-align: center; padding: 4rem 2rem;'>
    <h1 style='color: #2E8B57; font-size: 2.5rem; margin-bottom: 1rem;'>
        <i class="fa-solid fa-seedling"></i>
        Agriculture AI Assistant
    </h1>
    <p style='color: #666; font-size: 1.2rem;'>
        Select a page from the sidebar to begin your agricultural analysis
    </p>
</div>
""", unsafe_allow_html=True)
