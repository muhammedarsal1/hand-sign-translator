import streamlit as st
import streamlit.components.v1 as components

# HTML + JavaScript code for accessing the camera
camera_html = """
    <script>
        async function startCamera() {
            const video = document.getElementById("videoElement");
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
        }
        window.onload = startCamera;
    </script>
    <video id="videoElement" autoplay playsinline style="width: 100%;"></video>
"""

# Streamlit app
def show_camera():
    st.markdown("### 📷 Live Camera Feed")
    components.html(camera_html, height=400)

