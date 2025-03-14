import streamlit as st
import base64
import cv2
import numpy as np
from predictor import predict_sign  # Your ML model

# Load JavaScript for the camera
st.markdown("""
    <script src="/static/camera.js"></script>
""", unsafe_allow_html=True)

# HTML for camera stream
st.markdown("""
    <video id="video" autoplay playsinline style="width:100%;"></video>
    <canvas id="canvas" style="display:none;"></canvas>
    <button onclick="captureFrame()">📸 Capture Frame</button>
""", unsafe_allow_html=True)

# Handle incoming frames from JavaScript
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload_frame", methods=["POST"])
def upload_frame():
    data = request.json
    image_data = data.get("image", "")

    if not image_data:
        return jsonify({"error": "No image received"}), 400

    # Decode base64 image
    image_bytes = base64.b64decode(image_data.split(",")[1])
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Predict sign language gesture
    result = predict_sign(frame)

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
