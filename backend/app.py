from flask import Flask, render_template, request, jsonify
import os
from model import predict_image
from chatbot import get_response

app = Flask(__name__)
UPLOAD_FOLDER = "/tmp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/scanner", methods=["GET", "POST"])
def scanner():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded"
        file = request.files["image"]
        if file.filename == "":
            return "No file selected"
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        result, confidence = predict_image(path)
        return render_template("scanner.html", result=result, confidence=confidence, image=file.filename)
    return render_template("scanner.html")

@app.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/get_response", methods=["POST"])
def chatbot_response():
    user_msg = request.form["message"]
    response = get_response(user_msg)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
