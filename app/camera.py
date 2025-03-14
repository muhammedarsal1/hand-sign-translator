import cv2
import streamlit as st

def get_frame():
    cap = cv2.VideoCapture(0)  # Change to 1 or -1 if not working

    if not cap.isOpened():
        st.error("🚨 Camera not accessible. Please enable camera permissions.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("🚨 Failed to capture frame. Try again.")
        return None

    return frame
