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
    # Récupère la valeur de la clé "text" du corps de la requête
    text = request.form['text']

    # Traite les données de la manière souhaitée...

    # Renvoie une réponse au client
    return "Merci pour votre soumission : " + text

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
