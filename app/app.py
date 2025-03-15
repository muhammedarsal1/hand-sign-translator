import streamlit as st
import numpy as np
from predictor import predict_sign
from camera_component import camera_input

st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")

# Title
st.title("🤟 Hand Sign Language Translator")
st.write("Show a hand sign to the camera, and the app will translate it.")

# Camera Input
st.subheader("📷 Camera Feed")
camera_input()

# Placeholder for the translated text
prediction_text = st.empty()

# Process the prediction (Placeholder logic)
if st.button("Translate Sign"):
    st.warning("Processing image... (This feature needs backend integration)")
    # Ideally, we should capture an image from the camera and send it to `predict_sign()`
    # Here, we just simulate the output.
    prediction_text.success(f"Predicted Sign: {np.random.choice(['A', 'B', 'C', 'D'])}")  
