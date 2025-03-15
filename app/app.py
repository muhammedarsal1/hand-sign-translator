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

    # Camera Component
    image_data = camera_input()

    # Display captured image
    if image_data:
        st.image(image_data, caption="📸 Captured Image", use_column_width=True)

        # Translate Button
        if st.button("Translate Sign"):
            processed_image = process_image(image_data)

            if processed_image is not None:
                prediction = predict_sign(processed_image)
                st.subheader(f"🔠 Predicted Sign: **{prediction}**")
            else:
                st.error("Error processing the image. Please try again.")

if __name__ == "__main__":
    main()
