import os
import streamlit as st
import numpy as np
import cv2
import base64
from predictor import predict_sign
from camera_component import camera_input

# Force TensorFlow to use CPU (Fixes GPU error)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def process_image(image_data):
    """Convert base64 image to numpy array and process it."""
    try:
        if not image_data:
            st.error("❌ No image data received!")
            return None

        # Decode Base64 Image
        image_bytes = base64.b64decode(image_data.split(',')[1])
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if image is None:
            st.error("❌ Failed to decode image.")
            return None

        return image
    except Exception as e:
        st.error(f"❌ Error processing image: {e}")
        return None

def main():
    st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")
    st.title("🤟 Hand Sign Language Translator")
    st.write("Show a hand sign to the camera, then press 'Translate' to see the result.")

    # Initialize session state variables
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None
    if "predicted_letter" not in st.session_state:
        st.session_state.predicted_letter = ""

    # Camera Component (Capturing Image)
    st.write("📷 **Camera Feed:**")
    image_data = camera_input()  # Show camera input

    # **Fix: Ensure image is saved in session state when captured**
    if image_data:
        st.session_state.captured_image = image_data  # Store captured image
        st.image(image_data, caption="📸 Captured Image", use_column_width=True)

    # Show Translate button **only if image is captured**
    if st.session_state.captured_image:
        if st.button("Translate Sign"):
            st.write("🔄 Processing...")  # Show loading message
            processed_image = process_image(st.session_state.captured_image)

            if processed_image is not None:
                prediction = predict_sign(processed_image)  # Predict hand sign
                st.session_state.predicted_letter = prediction  # Store prediction in session state

    # Display Translation Below Camera **(Fix UI)**
    if st.session_state.predicted_letter:
        st.subheader(f"🔠 **Predicted Sign: {st.session_state.predicted_letter}**")

if __name__ == "__main__":
    main()
