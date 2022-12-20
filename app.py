from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_current_time():
    current_time = {"current_time": str(datetime.now())}
    return jsonify(current_time)

@app.route("/status")
def hello():
    return "ok"
