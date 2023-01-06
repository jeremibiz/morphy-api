# compose_flask/app.py
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import tensorflow as tf

app = Flask(__name__)
CORS(app, origins=['http://morphy.fr.to', 'https://morphy.fr.to'])

# Charger le modèle de deep learning pré-entraîné
model = tf.keras.models.load_model('inclusive-writing-model.h5')

# Définir la fonction de conversion de texte en écriture inclusive
def convert_text_to_inclusive_writing(input_text):
    # Prédire la sortie en utilisant le modèle de deep learning
    prediction = model.predict(input_text)

    # Convertir la prédiction en texte et renvoyer le résultat
    return prediction_to_text(prediction)


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
    output_text = convert_text_to_inclusive_writing(input_text)
    return "Merci pour votre soumission : " + output_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
