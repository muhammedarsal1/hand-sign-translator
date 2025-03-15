import os
import streamlit as st
import numpy as np
import cv2
import base64
import tensorflow as tf
from PIL import Image
from predictor import predict_sign
from camera_component import camera_input

# ✅ Ensure set_page_config is the first Streamlit command
st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")

# ✅ Force TensorFlow to use CPU (Fixes CUDA error)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# ✅ Initialize session state for storing image data
if "captured_image" not in st.session_state:
    st.session_state.captured_image = None

def process_image(image_data):
    """Convert base64 image to numpy array and preprocess for the model."""
    try:
        if not isinstance(image_data, str) or "," not in image_data:
            st.error("❌ Invalid image data received!")
            return None

        image_bytes = base64.b64decode(image_data.split(',')[1])
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)  # ✅ Convert to grayscale
        image = cv2.resize(image, (64, 64))  # ✅ Resize to match model input size
        image = image / 255.0  # ✅ Normalize pixel values
        image = np.expand_dims(image, axis=-1)  # ✅ Add channel dimension for model
        return image
    except Exception as e:
        st.error(f"❌ Image processing error: {e}")
        return None

def main():
    st.title("🤟 Hand Sign Language Translator")
    st.write("Show a hand sign to the camera, capture an image, and press 'Translate'.")

    # ✅ Get image data from JavaScript
    image_data = camera_input()

    if image_data and isinstance(image_data, str) and "," in image_data:
        st.session_state.captured_image = image_data
        st.image(image_data, caption="📸 Captured Image", use_container_width=True)
    else:
        st.warning("⚠️ No image captured yet. Please take a picture.")

    # ✅ Translate button
    if st.session_state.captured_image:
        if st.button("🔠 Translate Sign"):
            processed_image = process_image(st.session_state.captured_image)
            if processed_image is not None:
                prediction = predict_sign(processed_image)  # ✅ Get prediction
                st.subheader(f"🔠 Predicted Sign: **{prediction}**")
            else:
                st.error("❌ Unable to process image for translation.")

if __name__ == "__main__":
    main()
