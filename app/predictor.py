import tensorflow as tf
import json
import os

# Define model path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "sign_model.h5")
LABELS_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "labels.json")

# Check if model file exists before loading
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}. Please train the model first.")

# Load the model
model = tf.keras.models.load_model(MODEL_PATH)

# Load class labels
if not os.path.exists(LABELS_PATH):
    raise FileNotFoundError(f"Labels file not found: {LABELS_PATH}. Make sure it exists.")

with open(LABELS_PATH, "r") as file:
    labels = json.load(file)

def predict_sign(image):
    """
    Predicts the hand sign from the given image.
    :param image: Processed image for model inference.
    :return: Predicted sign label.
    """
    # Preprocess image for model input
    image = image / 255.0  # Normalize pixel values
    image = image.reshape(1, 64, 64, 1)  # Reshape for model (assuming 64x64 grayscale input)

    # Get predictions
    predictions = model.predict(image)
    predicted_label = labels[str(predictions.argmax())]

    return predicted_label
