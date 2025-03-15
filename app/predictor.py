import tensorflow as tf
import json
import os
import cv2
import numpy as np

# Define model and label paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "sign_model.h5")
LABELS_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "labels.json")

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}. Please train the model first.")
model = tf.keras.models.load_model(MODEL_PATH)

# Load labels
if not os.path.exists(LABELS_PATH):
    raise FileNotFoundError(f"Labels file not found: {LABELS_PATH}. Make sure it exists.")
with open(LABELS_PATH, "r") as file:
    labels = json.load(file)

def preprocess_image(image):
    """Convert image to grayscale, resize, normalize, and reshape for model input."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    image = cv2.resize(image, (64, 64))  # Resize to 64x64
    image = image / 255.0  # Normalize (0 to 1 range)
    image = image.reshape(1, 64, 64, 1)  # Reshape for model input
    return image

def predict_sign(image):
    """
    Predicts the hand sign from the given image.
    :param image: Captured image from camera.
    :return: Predicted sign label.
    """
    processed_image = preprocess_image(image)  # Preprocess image
    predictions = model.predict(processed_image)  # Get predictions
    predicted_label_index = int(np.argmax(predictions))  # Get highest confidence label
    predicted_label = labels.get(str(predicted_label_index), "Unknown")  # Get label or "Unknown"

    return predicted_label
