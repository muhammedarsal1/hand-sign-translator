import streamlit as st
import numpy as np
import cv2
import base64
from predictor import predict_sign
from camera_component import camera_input

def process_image(image_data):
    """Convert base64 image to numpy array and process it."""
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

def main():
    st.set_page_config(page_title="Hand Sign Language Translator", layout="wide")
    st.title("🤟 Hand Sign Language Translator")
    st.write("Show a hand sign to the camera, then press 'Translate' to see the result.")

    # Initialize session state for storing the image and prediction
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None
    if "predicted_letter" not in st.session_state:
        st.session_state.predicted_letter = ""

    # Camera Component
    image_data = camera_input()

    if image_data:
        st.session_state.captured_image = image_data  # Store captured image
        st.image(image_data, caption="📸 Captured Image", use_column_width=True)

    # Show Translate button only if an image is captured
    if st.session_state.captured_image:
        if st.button("Translate Sign"):
            processed_image = process_image(st.session_state.captured_image)
            st.session_state.predicted_letter = predict_sign(processed_image)  # Store prediction

    # Display the predicted letter **below** the camera
    if st.session_state.predicted_letter:
        st.subheader(f"🔠 Predicted Sign: **{st.session_state.predicted_letter}**")

if __name__ == "__main__":
    main()
