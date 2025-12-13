import streamlit as st
import sys, os

# Allow importing shared components
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from components.styles import create_progress_bar

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Soil Quality Analysis",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- STYLES ---------------- #
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

# ---------------- TITLE ---------------- #
st.markdown(
    '<div class="main-title"><i class="fa-solid fa-seedling"></i> Soil Quality Analysis</div>',
    unsafe_allow_html=True
)

# ---------------- AGRONOMIC THRESHOLDS ---------------- #
OPTIMAL = {
    "N": (50, 150),
    "P": (20, 60),
    "K": (80, 200),
    "pH": (6.2, 6.8)
}

MAX_VALUE = 500

# ---------------- HELPER FUNCTIONS ---------------- #
def nutrient_score(value, opt_min, opt_max, max_value):
    if value <= 0:
        return 0

    if value < opt_min:
        return (value / opt_min) * 100

    if opt_min <= value <= opt_max:
        return 100

    excess_ratio = (value - opt_max) / (max_value - opt_max)
    penalty = excess_ratio * 50
    return max(50, 100 - penalty)


def ph_score(ph):
    optimal = 6.5
    tolerance = 1.2
    diff = abs(ph - optimal)

    if diff <= tolerance:
        return 100
    return max(0, 100 - (diff - tolerance) * 40)


def nutrient_recommendation(value, opt_min, opt_max, nutrient):
    if value < opt_min:
        return (
            "warning",
            f"Deficient — Increase {nutrient} using organic compost "
            f"or balanced fertilizer."
        )

    if value > opt_max * 1.5:
        return (
            "error",
            f"Excessive — High {nutrient} may reduce nutrient uptake. "
            f"Pause {nutrient}-rich fertilizers and leach with irrigation."
        )

    return (
        "success",
        f"Optimal — {nutrient} level is suitable for healthy crop growth."
    )


def ph_recommendation(ph):
    if ph < OPTIMAL["pH"][0]:
        return (
            "error",
            "Acidic soil — Apply agricultural lime gradually and "
            "increase organic matter."
        )

    if ph > 7.5:
        return (
            "error",
            "Alkaline soil — Apply elemental sulfur or organic compost "
            "to improve nutrient availability."
        )

    return (
        "success",
        "Optimal pH — Soil supports maximum nutrient availability."
    )

# ---------------- INPUTS ---------------- #
st.markdown(
    '<div class="section-header"><i class="fa-solid fa-sliders"></i> Soil Parameter Input</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(
        '<div class="sub-header"><i class="fa-solid fa-flask"></i> Nutrient Levels (ppm)</div>',
        unsafe_allow_html=True
    )

    N = st.slider("Nitrogen (N)", 0, 500, 80)
    P = st.slider("Phosphorus (P)", 0, 500, 35)
    K = st.slider("Potassium (K)", 0, 500, 120)
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.5, 0.1)

# ---------------- SCORING ---------------- #
N_score = nutrient_score(N, *OPTIMAL["N"], MAX_VALUE)
P_score = nutrient_score(P, *OPTIMAL["P"], MAX_VALUE)
K_score = nutrient_score(K, *OPTIMAL["K"], MAX_VALUE)
PH_score = ph_score(ph)

soil_score = round(
    N_score * 0.30 +
    P_score * 0.20 +
    K_score * 0.20 +
    PH_score * 0.30,
    1
)

# ---------------- RESULTS ---------------- #
with col2:
    st.markdown(
        '<div class="sub-header"><i class="fa-solid fa-chart-line"></i> Analysis Results</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"### 🌱 Soil Quality Score: **{soil_score}/100**")
    st.markdown(create_progress_bar(soil_score, 100), unsafe_allow_html=True)

    if soil_score >= 85:
        st.success("Excellent — Soil conditions are ideal for most crops")
    elif soil_score >= 65:
        st.warning("Moderate — Soil is productive but improvable")
    else:
        st.error("Poor — Soil constraints limit crop productivity")

    st.markdown(
        '<div class="sub-header"><i class="fa-solid fa-leaf"></i> Nutrient Health</div>',
        unsafe_allow_html=True
    )

    for label, score in {
        "Nitrogen": N_score,
        "Phosphorus": P_score,
        "Potassium": K_score,
        "pH": PH_score
    }.items():
        st.markdown(f"**{label}**: {score:.1f}%")
        st.markdown(create_progress_bar(score, 100), unsafe_allow_html=True)

# ---------------- RECOMMENDATIONS ---------------- #
st.markdown(
    '<div class="section-header"><i class="fa-solid fa-bulb"></i> Agronomic Recommendations</div>',
    unsafe_allow_html=True
)

colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="sub-header">Soil pH</div>', unsafe_allow_html=True)
    status, msg = ph_recommendation(ph)
    getattr(st, status)(msg)

    st.markdown('<div class="sub-header">Nitrogen (N)</div>', unsafe_allow_html=True)
    status, msg = nutrient_recommendation(N, *OPTIMAL["N"], "Nitrogen")
    getattr(st, status)(msg)

with colB:
    st.markdown('<div class="sub-header">Phosphorus (P)</div>', unsafe_allow_html=True)
    status, msg = nutrient_recommendation(P, *OPTIMAL["P"], "Phosphorus")
    getattr(st, status)(msg)

    st.markdown('<div class="sub-header">Potassium (K)</div>', unsafe_allow_html=True)
    status, msg = nutrient_recommendation(K, *OPTIMAL["K"], "Potassium")
    getattr(st, status)(msg)
