from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field

# 1. Define the Input Schema with validation examples
# This is Pydantic - it ensures the API only accepts the right data types
class DiabetesInput(BaseModel):
    Pregnancies: int = Field(..., example=2)
    Glucose: float = Field(..., example=120.0)
    BloodPressure: float = Field(..., example=70.0)
    SkinThickness: float = Field(..., example=20.0)
    Insulin: float = Field(..., example=80.0)
    BMI: float = Field(..., example=25.5)
    DiabetesPedigreeFunction: float = Field(..., example=0.45)
    Age: int = Field(..., example=35)

# 2. Initialize FastAPI
app = FastAPI(
    title="Diabetes Prediction API",
    description="An Ensemble ML Model (XGBoost + Random Forest) for predicting diabetes.",
    version="1.0.0"
)

# 3. Load the Model Pipeline
# Important: The path must match your folder structure
try:
    model = joblib.load("model_bin/diabetes_model.joblib")
except Exception as e:
    print(f"Error loading model: {e}")

@app.get("/")
def home():
    return {
        "Project": "Diabetes Prediction Service",
        "Status": "Online",
        "Model_Type": "Ensemble (RF + XGBoost)",
        "Documentation": "/docs"
    }

@app.post("/predict")
def predict(data: DiabetesInput):
    try:
        # Convert Pydantic model to a Dictionary
        input_data = data.model_dump()
        
        # Convert dictionary to Pandas DataFrame (required by sklearn Pipeline)
        df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model.predict(df)[0]
        
        # Get probability (confidence)
        probabilities = model.predict_proba(df)[0]
        confidence = float(np.max(probabilities))
        
        return {
            "prediction": "Diabetic" if int(prediction) == 1 else "Healthy",
            "prediction_code": int(prediction),
            "confidence_score": round(confidence, 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))