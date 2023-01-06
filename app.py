# compose_flask/app.py
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://morphy.fr.to', 'https://morphy.fr.to'])

@app.route("/date")
def get_current_time():
    current_time = {"current_time": str(datetime.now())}
    return jsonify(current_time)

@app.route("/status")
def status():
    return jsonify(
        message="Morphy-API is alive.",
        status=200
    )

@app.route("/submit", methods=['POST'])
def submit():
    text = request.form['text']
    return "Merci pour votre soumission : " + text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
