from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Charger le pipeline
model = joblib.load('model_pipeline_threshold.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    # Probabilité de phishing
    proba = model.predict_proba([text])[0][1]
    label = 'Phishing' if proba >= 0.7 else 'Safe'

    return jsonify({'prediction': label, 'score': round(proba, 2)})

if __name__ == '__main__':
    print("✅ Serveur lancé sur http://localhost:5000")
    app.run(debug=True, port=5000)
