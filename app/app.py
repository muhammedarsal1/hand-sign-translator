import os
import streamlit as st
import numpy as np
import cv2
import base64
from predictor import predict_sign
from camera_component import camera_input

# Force TensorFlow to use CPU (Fix CUDA error)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def process_image(image_data):
    """Convert base64 image to numpy array and process it."""
    try:
        image_bytes = base64.b64decode(image_data.split(',')[1])
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

def main():
    st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")
    st.title("🤟 Hand Sign Language Translator")
    st.write("Show a hand sign to the camera, then press 'Translate' to see the result.")

    # Initialize session state
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None
    if "predicted_letter" not in st.session_state:
        st.session_state.predicted_letter
