import streamlit as st
from src.predict import predict_customer
from src.genai_report import generate_report

st.title("📊 Financial Marketing Analyzer")

age = st.number_input("Enter Age", min_value=18, max_value=100)
income = st.number_input("Enter Income")
loan = st.selectbox("Loan", ["Yes", "No"])

if st.button("Analyze"):
    prediction, segment = predict_customer(age, income, loan)

    result = "Will Buy" if prediction == 1 else "Will Not Buy"

    st.subheader("Prediction")
    st.write(result)

    st.subheader("Customer Segment")
    st.write(segment)

    # Generate AI report
    report = generate_report(age, income, loan, result, segment)

    st.subheader("AI Insights")
    st.write(report)