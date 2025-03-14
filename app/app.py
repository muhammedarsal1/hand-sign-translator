import streamlit as st
import cv2
import numpy as np
from camera import get_frame
from predictor import predict_sign

st.title("🤟 Hand Sign Language Translator")
st.write("Show a hand sign to the camera, and the app will translate it.")

# Open the webcam
FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("🚨 Camera not accessible. Please enable camera permissions.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Failed to capture frame. Restart the app.")
            break

        # Process and show the frame
        processed_frame = get_frame(frame)
        prediction = predict_sign(processed_frame)
        st.write(f"Predicted Sign: {prediction}")
        FRAME_WINDOW.image(frame, channels="BGR")
    
cap.release()
