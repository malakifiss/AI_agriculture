import streamlit as st
import pandas as pd
from io import BytesIO
from fpdf import FPDF
import sys
import os
import matplotlib
matplotlib.use("Agg")  # for headless environments (Streamlit)
import matplotlib.pyplot as plt
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Page Config
st.set_page_config(
    page_title="Crop Growing Guide",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/crop_yield.csv")

df = load_data()

# Load Font Awesome
st.markdown("""
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-header">
    <i class="fa-solid fa-seedling" 
       style="color: #2E8B57; margin-right: 10px;"></i>
    Crop Growing Guide
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='margin-bottom: 2rem;'>
    <p style='color: #666; line-height: 1.6;'>
        Comprehensive reference guide containing optimal growing conditions and requirements 
        for various agricultural crops based on extensive data analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
#  IMAGE / DIAGRAM HELPERS  (Magazine-style diagrams)
# ============================================================

def _save_fig_temp(fig):
    """Save a Matplotlib figure to a temporary PNG file and return its path."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmp.name, format="png", dpi=220, bbox_inches="tight")
    plt.close(fig)
    return tmp.name


def create_planting_season_diagram(crop_name, ideal_temp, ideal_rainfall):
    """Diagram for 'Best Planting Season' – shows suitability per season."""
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    # simple heuristic using temperature / rainfall
    scores = []
    for s in seasons:
        if s == "Spring":
            scores.append(9)
        elif s == "Autumn":
            scores.append(8)
        elif s == "Summer":
            scores.append(7 if ideal_temp < 32 else 5)
        else:  # Winter
            scores.append(4 if ideal_temp > 12 else 6)

    fig, ax = plt.subplots(figsize=(6, 3))
    bars = ax.bar(seasons, scores)
    ax.set_ylim(0, 10)
    ax.set_ylabel("Suitability")
    ax.set_title(f"Best Planting Season for {crop_name}")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.3,
                f"{int(b.get_height())}", ha="center", va="bottom", fontsize=8)

    return _save_fig_temp(fig)


def create_soil_profile_diagram(ideal_ph, N, P, K):
    """Diagram for 'Soil Preparation & Fertilization' – soil profile style."""
    fig, ax = plt.subplots(figsize=(5, 3))
    layers = ["Surface Organic Layer", "Topsoil (NPK)", "Subsoil", "Parent Material"]
    importance = [7, 9, 5, 3]

    ax.barh(layers, importance)
    ax.set_xlabel("Relative Importance")
    ax.set_title(f"Soil Profile & Fertilization Focus (pH={ideal_ph:.1f})")
    ax.invert_yaxis()
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    text = f"N≈{N:.0f}, P≈{P:.0f}, K≈{K:.0f}"
    ax.text(0.98, 0.05, text, transform=ax.transAxes,
            ha="right", va="bottom", fontsize=8,
            bbox=dict(boxstyle="round", alpha=0.1))

    return _save_fig_temp(fig)


def create_irrigation_schedule_diagram():
    """Diagram for 'Irrigation Schedule' – water demand per stage."""
    stages = ["Sowing", "Early Growth", "Flowering", "Grain Filling", "Maturity"]
    water_need = [7, 8, 10, 8, 5]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(stages, water_need, marker="o", linewidth=2)
    ax.set_ylim(0, 11)
    ax.set_ylabel("Relative Water Demand")
    ax.set_title("Irrigation Demand Across Growth Stages")
    ax.grid(True, linestyle="--", alpha=0.4)

    for x, y in zip(stages, water_need):
        ax.text(x, y + 0.3, str(y), ha="center", va="bottom", fontsize=8)

    return _save_fig_temp(fig)


def create_pests_treatment_diagram():
    """Diagram for 'Pests & Recommended Treatments' – IPM strategy mix."""
    strategies = ["Monitoring", "Cultural\nPractices", "Biological\nControl", "Chemical\nControl"]
    weight = [9, 7, 6, 4]

    fig, ax = plt.subplots(figsize=(5.5, 3))
    bars = ax.bar(strategies, weight)
    ax.set_ylim(0, 10)
    ax.set_ylabel("Recommended Priority")
    ax.set_title("Integrated Pest Management Strategy Mix")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.3,
                f"{int(b.get_height())}", ha="center", va="bottom", fontsize=8)

    return _save_fig_temp(fig)


def create_growth_stages_diagram():
    """Diagram for 'Growth Stages & Care Guide' – attention level across timeline."""
    stages = ["Emergence", "Tillering\n/Leafing", "Stem\nElongation", "Flowering", "Ripening"]
    attention = [9, 8, 8, 10, 6]

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.step(range(len(stages)), attention, where="mid", linewidth=2)
    ax.scatter(range(len(stages)), attention)
    ax.set_xticks(range(len(stages)))
    ax.set_xticklabels(stages)
    ax.set_ylim(0, 11)
    ax.set_ylabel("Management Attention")
    ax.set_title("Crop Growth Stages & Management Focus")
    ax.grid(True, linestyle="--", alpha=0.4)

    for i, val in enumerate(attention):
        ax.text(i, val + 0.3, str(val), ha="center", va="bottom", fontsize=8)

    return _save_fig_temp(fig)


# ============================================================
#  PDF GENERATION – RICH / PROFESSIONAL
# ============================================================

def generate_crop_pdf(crop_name, ideal, ranges, recommendation_text):
    """
    Build a PDF report for a given crop and return it as bytes.
    Includes rich illustrated diagrams for sections 3–7.
    """
    crop_name = crop_name.replace("–", "-")
    recommendation_text = recommendation_text.replace("–", "-")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, f"{crop_name} - Growing Report", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "This report summarizes the optimal environmental and soil conditions for this crop, "
        "including visual diagrams for key agronomic decisions (planting season, soil "
        "preparation, irrigation, pest management, and growth stages)."
    )

    # Section 1: Optimal Growing Conditions
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "1. Optimal Growing Conditions", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 7, f"- Temperature: {ideal['temperature']:.1f} °C", ln=True)
    pdf.cell(0, 7, f"- Humidity: {ideal['humidity']:.1f} %", ln=True)
    pdf.cell(0, 7, f"- Rainfall: {ideal['rainfall']:.1f} mm", ln=True)
    pdf.cell(0, 7, f"- Soil pH: {ideal['ph']:.1f}", ln=True)
    pdf.cell(0, 7, f"- Nitrogen (N): {ideal['N']:.1f}", ln=True)
    pdf.cell(0, 7, f"- Phosphorus (P): {ideal['P']:.1f}", ln=True)
    pdf.cell(0, 7, f"- Potassium (K): {ideal['K']:.1f}", ln=True)

    # Section 2: Observed Parameter Ranges
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "2. Observed Parameter Ranges", ln=True)

    pdf.set_font("Arial", "", 11)
    for label, (mn, mx, unit) in ranges.items():
        pdf.cell(0, 7, f"- {label}: {mn:.1f} - {mx:.1f}{unit}", ln=True)

    # ========= DIAGRAMS ==========

    # 3. Best Planting Season
    planting_img = create_planting_season_diagram(
        crop_name=crop_name,
        ideal_temp=ideal["temperature"],
        ideal_rainfall=ideal["rainfall"]
    )
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "3. Best Planting Season", ln=True)
    pdf.image(planting_img, x=15, w=180)
    pdf.ln(2)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "The diagram highlights which seasons offer the best match between temperature and "
        "rainfall for this crop. Prefer the seasons with the highest suitability scores for "
        "main sowing operations."
    )

    # 4. Soil Preparation & Fertilization
    soil_img = create_soil_profile_diagram(
        ideal_ph=ideal["ph"],
        N=ideal["N"],
        P=ideal["P"],
        K=ideal["K"]
    )
    pdf.add_page()
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "4. Soil Preparation & Fertilization", ln=True)
    pdf.image(soil_img, x=15, w=180)
    pdf.ln(2)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "The soil profile diagram illustrates which layers require the most attention. "
        "Focus on building organic matter in the surface horizon, maintaining pH in the "
        "optimal range, and applying balanced NPK fertilization according to soil tests "
        "and local recommendations."
    )

    # 5. Irrigation Schedule
    irrig_img = create_irrigation_schedule_diagram()
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "5. Irrigation Schedule", ln=True)
    pdf.image(irrig_img, x=15, w=180)
    pdf.ln(2)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "Water demand varies with the growth stage. The curve shows higher requirements "
        "during early growth and flowering. Maintain soil moisture near field capacity "
        "in these phases and avoid both drought stress and waterlogging."
    )

    # 6. Pests & Recommended Treatments
    pest_img = create_pests_treatment_diagram()
    pdf.add_page()
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "6. Pests & Recommended Treatments", ln=True)
    pdf.image(pest_img, x=15, w=180)
    pdf.ln(2)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "The IPM strategy mix diagram emphasizes preventive monitoring and cultural "
        "practices, supported by biological control. Chemical treatments should be used "
        "as a last resort, targeted and compliant with local regulations."
    )

    # 7. Growth Stages & Care Guide
    growth_img = create_growth_stages_diagram()
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "7. Growth Stages & Care Guide", ln=True)
    pdf.image(growth_img, x=15, w=180)
    pdf.ln(2)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "Management intensity should be highest from emergence to flowering. The diagram "
        "shows where weed control, nutrition, and irrigation have the greatest impact on "
        "yield formation."
    )

    # 8. Harvesting & Yield
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "8. Harvesting Recommendations & Yield", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(
        0, 6,
        "Harvest at physiological maturity for maximum grain quality. Avoid delays that "
        "increase shattering or lodging risks. Yield will depend on variety, climate, "
        "and how closely the above recommendations are followed."
    )

    # 9. Platform Recommendations
    pdf.ln(4)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "9. Platform Recommendations", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6, recommendation_text)

    # Export to bytes
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer.getvalue()


# ============================================================
#  MAIN STREAMLIT UI
# ============================================================

crops = sorted(df["label"].unique())
selected_crop = st.selectbox(
    "Select Crop",
    crops,
    help="Choose a crop to view detailed growing information"
)

if selected_crop:
    crop_data = df[df["label"] == selected_crop]
    ideal = crop_data.mean(numeric_only=True)

    st.markdown("---")

    # Crop Information
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            f'<div class="section-header">{selected_crop} - Growing Conditions</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="subsection-header">Optimal Parameter Ranges</div>',
            unsafe_allow_html=True
        )

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
        st.markdown(
            '<div class="subsection-header">Crop Statistics</div>',
            unsafe_allow_html=True
        )

        st.metric("Data Samples", len(crop_data))

        # Ranges (shared with PDF)
        st.markdown("**Parameter Ranges:**")
        ranges = {}
        for col, label, unit in [
            ("temperature", "Temperature (°C)", "°C"),
            ("humidity", "Humidity (%)", "%"),
            ("ph", "Soil pH", ""),
        ]:
            min_val = crop_data[col].min()
            max_val = crop_data[col].max()
            st.write(f"**{label}**: {min_val:.1f} - {max_val:.1f}{unit}")
            ranges[label] = (min_val, max_val, unit)

        # Growing Recommendations (used also in PDF)
        st.markdown(
            '<div class="subsection-header">Growing Recommendations</div>',
            unsafe_allow_html=True
        )

        if selected_crop.lower() in ["rice", "wheat"]:
            recommendation_text = (
                "This crop requires a consistent water supply and prefers warm "
                "temperatures. Ensure well-drained fields, regular irrigation, "
                "and close monitoring of nutrient levels for best results."
            )
            st.info(
                "**Key Requirements:**\n"
                "- Consistent water supply essential\n"
                "- Prefers warm growing temperatures\n"
                "- Well-drained soil conditions\n"
                "- Regular nutrient monitoring\n"
            )
        elif selected_crop.lower() in ["maize", "corn"]:
            recommendation_text = (
                "Plant in warm soil with full sunlight exposure. Maintain a "
                "regular irrigation schedule and pay particular attention to "
                "soil fertility during early growth and flowering."
            )
            st.info(
                "**Key Requirements:**\n"
                "- Plant in warm soil conditions\n"
                "- Requires full sunlight exposure\n"
                "- Regular irrigation important\n"
                "- Soil fertility management\n"
            )
        else:
            recommendation_text = (
                "Maintain balanced soil moisture and conduct periodic soil "
                "tests. Keep pH within the recommended range and apply "
                "balanced fertilization according to crop needs."
            )
            st.info(
                "**General Guidelines:**\n"
                "- Monitor soil moisture levels\n"
                "- Regular soil testing recommended\n"
                "- Adjust pH as necessary\n"
                "- Balanced nutrient application\n"
            )

    # ---------- PDF generation button ---------- #
    st.markdown("---")
    st.subheader("📄 Export Crop Report")

    if st.button("Generate PDF Report"):
        pdf_bytes = generate_crop_pdf(
            crop_name=selected_crop,
            ideal=ideal,
            ranges=ranges,
            recommendation_text=recommendation_text,
        )

        st.download_button(
            label="⬇️ Download Crop Growing Report (PDF)",
            data=pdf_bytes,
            file_name=f"{selected_crop}_growing_report.pdf",
            mime="application/pdf"
        )