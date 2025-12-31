from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ ADD THIS
from services.ai_service import analyze_image
import os

app = Flask(__name__)
CORS(app)  # ✅ ADD THIS LINE

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(path)

    result = analyze_image(path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
