import pickle
from pathlib import Path
import numpy as np


MODEL_PATH = Path(__file__).parent.parent / "model" / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
    

def predict_salary(experience_years: float) -> float:
    """
    Predict salary based on years of experince
    """
    
    prediction = model.predict(np.array([[experience_years]]))
    
    print(prediction)
    return float(prediction[0])