# compose_flask/app.py
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, origins=['http://morphy.fr.to', 'https://morphy.fr.to'])

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='image/favicon.ico')

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
    input_text = request.form['text']
    return "Merci pour votre soumission : " + input_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
