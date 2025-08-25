import random

def predict_image(path):
    diseases = ["Healthy Crop 🌱", "Leaf Spot 🍂", "Rust 🍃", "Blight 🌾"]
    result = random.choice(diseases)
    confidence = round(random.uniform(75, 98), 2)
    return result, confidence
