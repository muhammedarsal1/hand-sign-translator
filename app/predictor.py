import tensorflow as tf
import numpy as np
import json
import cv2

# Load model and labels
MODEL_PATH = "model/sign_model.h5"
LABELS_PATH = "model/labels.json"

model = tf.keras.models.load_model(MODEL_PATH)
with open(LABELS_PATH, "r") as f:
    labels = json.load(f)

def predict_sign(image):
    image = cv2.resize(image, (64, 64))
    image = np.expand_dims(image, axis=0) / 255.0
    prediction = model.predict(image)
    sign = labels[str(np.argmax(prediction))]
    return sign
