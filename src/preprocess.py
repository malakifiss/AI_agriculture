import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)
    return df

def split_features_labels(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    return X, y
