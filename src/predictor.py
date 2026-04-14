import joblib
import os
import numpy as np

# Load and prepare the model and scaler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "nasa_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")
features_path = os.path.join(BASE_DIR, "models", "features.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
features_list = joblib.load(features_path)

def predict(data):
    # Extract features in the correct order
    input_data = [data[f] for f in features_list]
    
    # Scale the input
    input_scaled = scaler.transform([input_data])
    
    pred = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    return pred, probability