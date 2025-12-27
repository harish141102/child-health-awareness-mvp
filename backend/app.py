from flask import Flask, request, jsonify
from flask_cors import CORS
import os

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

    # Dummy AI response
    return jsonify({
        "status": "success",
        "message": "Image received",
        "risk_level": "Medium",
        "note": "This is early awareness, not diagnosis"
    })

if __name__ == '__main__':
    app.run(debug=True)
