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

    # Initialize session state for image storage
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None

    # Camera Component
    image_data = camera_input()

    if image_data:
        st.session_state.captured_image = image_data  # Store captured image
        st.image(image_data, caption="📸 Captured Image", use_column_width=True)

    # Show Translate button only if an image is captured
    if st.session_state.captured_image:
        if st.button("Translate Sign"):
            st.write("🔄 Processing image...")  # Show processing message
            processed_image = process_image(st.session_state.captured_image)

            if processed_image is not None:
                prediction = predict_sign(processed_image)  # Get prediction
                if prediction:
                    st.subheader(f"🔠 Predicted Sign: **{prediction}**")
                else:
                    st.error("❌ Unable to recognize the sign. Please try again.")
            else:
                st.error("❌ Image processing failed. Capture a new image.")

if __name__ == "__main__":
    main()
