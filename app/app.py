import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU to avoid CUDA errors

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from predictor import predict_sign
from camera_component import camera_input

# Load model and labels
model = tf.keras.models.load_model("model/sign_model.h5")
with open("model/labels.json", "r") as f:
    labels = {int(k): v for k, v in json.load(f).items()}

st.title("Hand Sign Language Translator")
st.write("Upload an image or use the webcam to detect hand signs.")

# Camera input
image = camera_input()

if image is not None:
    st.image(image, caption="Captured Image", use_column_width=True)
    label, confidence = predict_sign(image, model, labels)
    st.write(f"Prediction: {label} (Confidence: {confidence:.2f}%)")

# File uploader option
uploaded_file = st.file_uploader("Or upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    label, confidence = predict_sign(image, model, labels)
    st.write(f"Prediction: {label} (Confidence: {confidence:.2f}%)")
