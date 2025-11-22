import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
from src.preprocess import load_dataset, split_features_labels

def train_model():
    df = load_dataset("data/crop_yield.csv")

    X, y = split_features_labels(df, target_column="yield")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print("Model trained ➤ MSE:", mse)

    joblib.dump(model, "models/crop_yield_model.pkl")
    print("Model saved to /models/crop_yield_model.pkl")

if __name__ == "__main__":
    train_model()
