import streamlit as st
import numpy as np
import cv2
import base64
from predictor import predict_sign
from camera_component import camera_input

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

    # Initialize session state variables
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None
    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    # Camera Component
    image_data = camera_input()

    if image_data:
        st.session_state.captured_image = image_data  # Store captured image
        st.image(image_data, caption="📸 Captured Image", use_column_width=True)

    # Show Translate button only if an image is captured
    if st.session_state.captured_image:
        if st.button("Translate Sign"):
            processed_image = process_image(st.session_state.captured_image)

            if processed_image is not None:
                prediction = predict_sign(processed_image)  # Get prediction
                st.session_state.prediction = prediction
            else:
                st.session_state.prediction = "Error: Could not process image."

    # Display the predicted sign below the camera section
    if st.session_state.prediction:
        st.subheader(f"🔠 Predicted Sign: **{st.session_state.prediction}**")

if __name__ == "__main__":
    main()
