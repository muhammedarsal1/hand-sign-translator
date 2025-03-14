import streamlit as st
import cv2
import numpy as np
from camera import get_frame
from predictor import predict_sign
from utils import preprocess_image

st.title("Hand Sign Language Translator")

# Start webcam
FRAME_WINDOW = st.image([])
st.write("Show a sign to the camera.")

while True:
    frame = get_frame()
    if frame is not None:
        processed_frame = preprocess_image(frame)
        FRAME_WINDOW.image(processed_frame, channels="RGB")
        
        # Predict sign
        sign = predict_sign(processed_frame)
        st.write(f"Predicted Sign: {sign}")
