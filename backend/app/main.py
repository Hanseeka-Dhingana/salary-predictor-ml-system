from fastapi import FastAPI, HTTPException
from model import predict_salary
from pydantic import BaseModel


app = FastAPI(title = "Salary Predictor API", description = "API to predict salary based on years of experience", version = "1.0.0")

@app.get("/")
def root():
    return {"message":"Welcome to the Salary Predictor API."}


class SalaryInput(BaseModel):
    experience_years: float

@app.post("/predict")
def predict(data : SalaryInput):
    '''
      Predict salary based on years of experience
    '''
    try: 
        salary = predict_salary(data.experience_years)
        return {"predicted_salary": salary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    