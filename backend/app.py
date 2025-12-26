from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/analyze-image", methods=["POST"])
def analyze_image():
    return jsonify({
        "risk": "At Risk",
        "confidence": "0.75"
    })

if __name__ == "__main__":
    app.run(debug=True)
