import joblib
import pandas as pd

def load_model():
    return joblib.load("models/crop_yield_model.pkl")

def predict_crop_yield(input_data: dict):
    model = load_model()
    
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    
    return prediction
