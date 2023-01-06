# compose_flask/app.py
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import tensorflow as tf

app = Flask(__name__)
CORS(app, origins=['http://morphy.fr.to', 'https://morphy.fr.to'])

model = tf.keras.models.load_model('inclusive-writing-model.h5')

def convert_text_to_inclusive_writing(input_text):
    prediction = model.predict(input_text)
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
