import cv2
import streamlit as st

def get_frame():
    # Try multiple camera indexes
    cap = None
    for i in [0, 1, -1]:  # Try different camera sources
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            break

    if not cap or not cap.isOpened():
        st.error("🚨 Camera not accessible. Please enable camera permissions.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("🚨 Failed to capture frame. Try again.")
        return None

    return frame
