import cv2
import numpy as np
import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification

model_name_or_path = "dima806/facial_emotions_image_detection" 
extractor = AutoFeatureExtractor.from_pretrained(model_name_or_path)
model = AutoModelForImageClassification.from_pretrained(model_name_or_path)
model.eval()

labels = model.config.id2label

def preprocess(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    inputs = extractor(images=rgb, return_tensors="pt")
    return inputs

def predict_emotion(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    inputs = preprocess(frame)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    return labels[predicted_class]
