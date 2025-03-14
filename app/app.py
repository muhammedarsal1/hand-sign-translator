import streamlit as st
from camera_component import show_camera

st.title("🤟 Hand Sign Language Translator")
st.write("Show a hand sign to the camera, and the app will translate it.")

# Display the camera
show_camera()
