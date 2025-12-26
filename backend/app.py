from flask import Flask
from routes.api import api_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint)

@app.route("/")
def home():
    return "Backend is running"

if __name__ == "__main__":
    app.run(debug=True)
