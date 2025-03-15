import os
import streamlit as st
import numpy as np
import cv2
import base64
from predictor import predict_sign
from camera_component import camera_input

# Force TensorFlow to use CPU
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
    st.write("Show a hand sign to the camera, then press 'Capture Image' and 'Translate' to see the result.")

    # Initialize session state variables
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None
    if "predicted_letter" not in st.session_state:
        st.session_state.predicted_letter = ""

    # Display Camera Component
    image_data = camera_input()

    # Capture Image Button
    if st.button("Capture Image"):
        if image_data:
            st.session_state.captured_image = image_data  # Store image in session state
            st.image(image_data, caption="📸 Captured Image", use_column_width=True)
        else:
            st.error("❌ No image captured! Please try again.")

    # Translate Button (Only Appears After Capturing an Image)
    if st.session_state.captured_image:
        if st.button("Translate Sign"):
            st.write("🔄 Processing...")
            processed_image = process_image(st.session_state.captured_image)

            if processed_image is not None:
                prediction = predict_sign(processed_image)
                st.session_state.predicted_letter = prediction
                st.subheader(f"🔠 **Predicted Sign: {prediction}**")

if __name__ == "__main__":
    main()
