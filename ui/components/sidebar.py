import streamlit as st

def show_sidebar():
    """Display the navigation sidebar"""
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 1.5rem 1rem; border-bottom: 1px solid #E0E0E0;'>
        <h2 style='color: #2E8B57; margin: 0; font-size: 1.5rem;'>Agriculture AI</h2>
        <p style='color: #666; margin: 0.5rem 0 0 0; font-size: 0.9rem;'>Smart Farming Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div style='padding: 1rem 0;'>
        <p style='color: #666; font-size: 0.9rem; margin-bottom: 1rem;'>
            Navigate through different sections to analyze and optimize your agricultural operations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Footer
    st.sidebar.markdown("""
    <div style='text-align: center; color: #999; padding: 1rem; font-size: 0.8rem;'>
        <p>Agriculture AI Assistant v1.0</p>
    </div>
    """, unsafe_allow_html=True)