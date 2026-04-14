import os
import pickle
import numpy as np

# Load models
clf = pickle.load(open("models/classifier.pkl", "rb"))
kmeans = pickle.load(open("models/clustering.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
if not os.path.exists("models/classifier.pkl"):
    raise Exception("Model not found! Run train_model.py first.")

def predict_customer(age, income, loan):
    loan_val = 1 if loan == "Yes" else 0

    data = np.array([[age, income, loan_val]])
    data_scaled = scaler.transform(data)

    prediction = clf.predict(data_scaled)[0]
    segment = kmeans.predict(data_scaled)[0]

    return prediction, segment