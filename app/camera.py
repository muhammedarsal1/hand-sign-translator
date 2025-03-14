import cv2
import streamlit as st

def get_frame():
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
    if not cap.isOpened():
        st.error("Could not open webcam. Please allow camera access.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("Failed to capture image from camera.")
        return None

    return frame
