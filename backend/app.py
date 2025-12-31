ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from services.ai_service import analyze_image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def home():
    return "CareLens Backend Running"

# Image upload route
@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(save_path)

    try:
        # 🔥 REAL AZURE AI CALL
        result = analyze_image(save_path)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": "AI processing failed"}), 500


if __name__ == '__main__':
    app.run(debug=True)
