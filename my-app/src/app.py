from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.environ.get("VERSION", "unknown")
    return f"Blue-Green Deployment App — version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
