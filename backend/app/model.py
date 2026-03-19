import pickle
from pathlib import Path
import pandas as pd


MODEL_PATH = Path(__file__).parent.parent / "model" / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
    

def predict_salary(experience_years: float) -> float:
    df = pd.DataFrame({
        "YearsExperience": [experience_years]
    })
    
    prediction = model.predict(df)
    return float(prediction[0])