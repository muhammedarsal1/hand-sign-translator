import streamlit as st
import numpy as np
import cv2
import base64
import tensorflow as tf
from predictor import predict_sign
from camera_component import camera_input

# Ensure TensorFlow runs on CPU
tf.config.set_visible_devices([], 'GPU')

def process_image(image_data):
    """Convert base64 image to numpy array and preprocess for the model."""
    try:
        image_bytes = base64.b64decode(image_data.split(',')[1])
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (64, 64))  # Ensure it matches model input size
        image = image / 255.0  # Normalize
        image = np.expand_dims(image, axis=-1)  # Add channel dimension
        return image
    except Exception as e:
        st.error(f"Image processing error: {e}")
        return None

def main():
    st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")
    st.title("🤟 Hand Sign Language Translator")
    st.write("Show a hand sign to the camera, capture an image, and press 'Translate'.")

    # Camera Input
    image_data = camera_input()

    # Display the captured image and provide translation
    if image_data:
        st.session_state["captured_image"] = image_data
        st.image(image_data, caption="📸 Captured Image", use_container_width=True)

    if "captured_image" in st.session_state and st.session_state["captured_image"]:
        if st.button("Translate Sign"):
            processed_image = process_image(st.session_state["captured_image"])
            if processed_image is not None:
                prediction = predict_sign(processed_image)  # Run ML model
                st.subheader(f"🔠 Predicted Sign: **{prediction}**")
            else:
                st.error("❌ No valid image captured! Please try again.")

if __name__ == "__main__":
    main()
