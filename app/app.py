import os
import streamlit as st
import cv2
import numpy as np
from predictor import predict_hand_sign
from camera_component import capture_image

# Disable GPU usage to avoid CUDA-related errors
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

st.title("Hand Sign Language Translator")

# Initialize camera
frame = capture_image()

if frame is not None:
    st.image(frame, channels="BGR")
    
    if st.button("Translate"):
        prediction = predict_hand_sign(frame)
        st.write(f"Predicted Sign: {prediction}")
