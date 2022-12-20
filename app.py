# compose_flask/app.py
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_current_time():
    current_time = {"current_time": str(datetime.now())}
    return jsonify(current_time)

@app.route("/status")
def status():
    return jsonify(
        message="Morphy-API is alive.",
        status=200
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
