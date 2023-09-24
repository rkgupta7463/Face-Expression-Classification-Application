import os
from flask import Flask, request, jsonify,render_template
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch

app = Flask(__name__)

# Load the model and extractor
model_path = "trpakov/vit-face-expression"
extractor = AutoFeatureExtractor.from_pretrained(model_path)
model = AutoModelForImageClassification.from_pretrained(model_path)

# Define a function to perform inference
def classify_image(image):
    inputs = extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    softmax = torch.nn.Softmax(dim=1)
    probs = softmax(logits)
    labels = model.config.id2label
    label_probabilities = [(labels[i], prob.item()) for i, prob in enumerate(probs[0])]
    label_probabilities.sort(key=lambda x: x[1], reverse=True)
    return label_probabilities


@app.route("/")
def home():
    return render_template("index.html")
# Define a route for image classification
@app.route("/classify", methods=["GET","POST"])
def classify():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"})

    image = Image.open(request.files["image"])
    results = classify_image(image)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True,port=5000)
