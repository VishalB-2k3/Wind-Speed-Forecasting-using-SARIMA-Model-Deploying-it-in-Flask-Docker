from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('sarimax_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Assuming data comes in JSON format with 'time' key
    time = data['time']
    # Perform any necessary preprocessing
    # Example: Convert 'time' to datetime if needed
    # Make prediction
    pred = loaded_model.get_forecast(steps=1).predicted_mean[0]
    return jsonify({'prediction': pred})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
