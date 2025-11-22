def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
        /* Main styling */
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #2E8B57;
            text-align: center;
            margin-bottom: 1rem;
            padding: 1rem;
            border-bottom: 3px solid #4CAF50;
        }
        
        .section-header {
            font-size: 1.8rem;
            font-weight: 600;
            color: #2E8B57;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #E0E0E0;
        }
        
        .subsection-header {
            font-size: 1.3rem;
            font-weight: 600;
            color: #455A64;
            margin: 1.5rem 0 1rem 0;
        }
        
        /* Feature cards */
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid #E0E0E0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            border-color: #4CAF50;
        }
        
        /* Metric cards */
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            margin: 0.5rem;
            min-height: 120px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        .metric-card h3 {
            font-size: 1.8rem;
            margin: 0;
            font-weight: bold;
        }
        
        .metric-card p {
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
            font-size: 0.9rem;
        }
        
        /* Button styling */
        .primary-button {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .primary-button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
        }
        
        /* Success and info boxes */
        .success-box {
            background: linear-gradient(135deg, #4CAF50, #45a049);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin: 1rem 0;
        }
        
        .info-box {
            background: #E3F2FD;
            border-left: 4px solid #2196F3;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        /* Progress bars */
        .progress-container {
            background: #f5f5f5;
            border-radius: 8px;
            height: 16px;
            margin: 0.5rem 0;
            overflow: hidden;
        }
        
        .progress-bar {
            height: 100%;
            background: linear-gradient(45deg, #4CAF50, #45a049);
            border-radius: 8px;
            transition: width 0.3s ease;
        }
        
        /* Input styling */
        .stNumberInput input, .stSlider input {
            border-radius: 6px;
            border: 1px solid #E0E0E0;
        }
        
        .stNumberInput input:focus, .stSlider input:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.1);
        }
        
        /* Remove Streamlit default styling */
        .main .block-container {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

def create_progress_bar(value, max_value=100):
    """Create a custom progress bar"""
    percentage = min(100, (value / max_value) * 100)
    return f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {percentage}%;"></div>
    </div>
    <div style="text-align: center; font-size: 0.8rem; color: #666; margin-top: 0.25rem;">
        {value}/{max_value} ({percentage:.1f}%)
    </div>
    """

def create_metric_card(value, label):
    """Create a metric card with value and label"""
    return f"""
    <div class="metric-card">
        <h3>{value}</h3>
        <p>{label}</p>
    </div>
    """

def create_feature_card(title, description, icon=None):
    """Create a feature card"""
    icon_html = f"<div style='font-size: 2rem; text-align: center; margin-bottom: 1rem;'>{icon}</div>" if icon else ""
    return f"""
    <div class="feature-card">
        {icon_html}
        <h4 style='margin: 0 0 0.5rem 0; color: #2E8B57;'>{title}</h4>
        <p style='margin: 0; color: #666; line-height: 1.5;'>{description}</p>
    </div>
    """