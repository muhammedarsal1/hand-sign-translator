import tensorflow as tf
import json
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "sign_model.h5")
LABELS_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "labels.json")

# Force TensorFlow to use CPU
tf.config.set_visible_devices([], 'GPU')

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)

# Load class labels
with open(LABELS_PATH, "r") as file:
    labels = json.load(file)

def predict_sign(image):
    """Predict the hand sign from the image."""
    image = np.expand_dims(image, axis=0)  # Reshape for model
    predictions = model.predict(image)
    predicted_label = labels[str(predictions.argmax())]
    return predicted_label
