import joblib
import numpy as np

def load_model():
    model = joblib.load("models/crop_yield_model.pkl")
    encoder = joblib.load("models/label_encoder.pkl")
    return model, encoder

def predict_crop(input_data):
    model, encoder = load_model()

    features = np.array([[
        input_data["N"],
        input_data["P"],
        input_data["K"],
        input_data["temperature"],
        input_data["humidity"],
        input_data["ph"],
        input_data["rainfall"]
    ]])

    prediction = model.predict(features)[0]
    crop_name = encoder.inverse_transform([prediction])[0]
    return crop_name
