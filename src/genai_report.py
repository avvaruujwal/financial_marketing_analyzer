def generate_report(age, income, loan, prediction, segment):
    
    # Simple AI-like logic (no API)
    if prediction == "Will Buy":
        decision = "This customer is likely to purchase financial products."
    else:
        decision = "This customer is less likely to respond to marketing."

    if income > 50000:
        income_level = "high income"
    else:
        income_level = "moderate income"

    if segment == 0:
        segment_type = "Low-value customer"
    elif segment == 1:
        segment_type = "Medium-value customer"
    else:
        segment_type = "High-value customer"

    report = f"""
    📊 Customer Analysis Report

    - Age: {age}
    - Income: {income} ({income_level})
    - Loan Status: {loan}
    - Segment: {segment_type}

     Prediction:
    {decision}

     Marketing Suggestion:
    Offer personalized financial products and targeted campaigns.
    """

    return report