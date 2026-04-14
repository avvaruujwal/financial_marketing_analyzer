from fastapi import FastAPI
from src.predict import predict_customer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Marketing API"}

@app.get("/predict")
def predict(age: int, income: int, loan: str):
    prediction, segment = predict_customer(age, income, loan)
    return {
        "prediction": int(prediction),
        "segment": int(segment)
    }