from flask import Blueprint, request, jsonify
import os

api_blueprint = Blueprint("api", __name__)

UPLOAD_FOLDER = "uploads"

@api_blueprint.route("/analyze-image", methods=["POST"])
def analyze_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    return jsonify({
        "risk": "At Risk",
        "confidence": "0.75"
    })
