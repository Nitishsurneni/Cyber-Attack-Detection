# src/pipeline/prediction_pipeline.py

import pickle
import numpy as np
import pandas as pd
import os

# Load the model
MODEL_PATH = os.path.join("Models", "xgboost_model.pkl")
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

def predict_attack(input_data: pd.DataFrame):
    """
    Predict whether a session is an attack or not.
    Args:
        input_data (pd.DataFrame): One or more rows with same features used during training.
    Returns:
        np.array: Predictions (0 = normal, 1 = attack)
    """
    return model.predict(input_data)
