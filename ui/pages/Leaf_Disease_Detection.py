import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
import os

# ==============================================================
# Load Model
# ==============================================================
MODEL_PATH = os.path.join("models", "plant_disease_model.h5")

@st.cache_resource
def load_disease_model():
    return load_model(MODEL_PATH)

model = load_disease_model()

CLASS_NAMES = (
    'Tomato-Bacterial_spot',
    'Potato-Barly blight',
    'Corn-Common_rust'
)

# ==============================================================
# UI Styling
# ==============================================================
st.set_page_config(page_title="Leaf Disease Detection", page_icon="🌱", layout="wide")

st.markdown("""
<link rel="stylesheet" 
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
.title {
    font-size: 42px;
    font-weight: 900;
    color: #2E8B57;
}
.upload-box {
    border: 2px dashed #2E8B57;
    padding: 20px;
    border-radius: 15px;
    background: #f7fff8;
}
.result-box {
    border-radius: 12px;
    padding: 18px;
    background: #ffffff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================
# Page Layout
# ==============================================================
st.markdown('<div class="title"><i class="fa-solid fa-leaf"></i> Leaf Disease Detection</div>',
            unsafe_allow_html=True)

st.write(" Upload a leaf image & get instant disease diagnosis")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    plant_image = st.file_uploader("Upload Leaf Image", type=["jpg", "jpeg", "png"])
    submit = st.button("Analyze Image")
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================
# Prediction
# ==============================================================
if submit:
    if plant_image is None:
        st.error("Please upload an image first.")
    else:
        # Convert → OpenCV
        data = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        resized = cv2.resize(image, (256, 256)).reshape((1, 256, 256, 3))

        # Show uploaded image
        st.image(image, channels="BGR", caption="Uploaded Leaf", use_column_width=True)

        # Prediction
        prediction = model.predict(resized)
        result_name = CLASS_NAMES[np.argmax(prediction)]
        crop, disease = result_name.split("-")

        # Result display
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader(" Diagnosis Result")

        st.write(f"** Plant Type:** `{crop}`")
        st.write(f"** Detected Disease:** `{disease}`")

        if "healthy" in disease.lower():
            st.success(" Great news! The plant is **HEALTHY** and thriving 🌱")
        else:
            st.error(f" Disease Detected: **{disease}**")
            st.info("""
### Recommended Actions
- Remove and destroy affected leaves  
- Improve spacing for better airflow  
- Avoid watering leaves directly  
- Apply proper fungicides / treatments  
""")
        st.markdown('</div>', unsafe_allow_html=True)
