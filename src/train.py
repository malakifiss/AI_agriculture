import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    # Load dataset
    df = pd.read_csv("data/crop_yield.csv")

    # Features
    X = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]

    # Target label (vegetable type)
    y = df["label"]

    # Encode labels (tomato = 0, onion = 1, etc.)
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # Create models folder if missing
    os.makedirs("models", exist_ok=True)

    # Save model & encoder
    joblib.dump(model, "models/crop_yield_model.pkl")
    joblib.dump(encoder, "models/label_encoder.pkl")

    print("Model and encoder saved successfully.")

if __name__ == "__main__":
    train_model()
