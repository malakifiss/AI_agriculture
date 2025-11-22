import joblib
import numpy as np

def load_model():
    model = joblib.load("models/crop_classifier.pkl")
    encoder = joblib.load("models/label_encoder.pkl")
    return model, encoder

def predict_crop(features):
    model, encoder = load_model()

    X = np.array([
        [
            features["N"],
            features["P"],
            features["K"],
            features["temperature"],
            features["humidity"],
            features["ph"],
            features["rainfall"]
        ]
    ])

    prediction = model.predict(X)
    crop = encoder.inverse_transform(prediction)[0]

    return crop
