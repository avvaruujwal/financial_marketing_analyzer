# 📊 Financial Marketing Analyzer (ML + GenAI)

##  Project Overview

The **Financial Marketing Analyzer** is a machine learning and AI-based system designed to analyze customer financial data, predict purchase behavior, and generate intelligent marketing insights.

This project combines:

* Machine Learning (Prediction & Clustering)
* Generative AI (Automated Insights)
* Interactive Dashboard (Streamlit)

---

##  Objectives

* Predict whether a customer will purchase a financial product
* Segment customers into different categories
* Generate AI-based marketing insights
* Help businesses make data-driven decisions

---

##  Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **AI Integration:** OpenAI API / Rule-based GenAI

---

## 📁 Project Structure

```
financial_marketing_analyzer/
│
├── data/                  # Dataset
├── models/                # Trained models (ignored in Git)
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   └── genai_report.py
│
├── report/                # Project report
├── app.py                 # Streamlit UI
├── api.py                 # FastAPI backend
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/financial_marketing_analyzer.git
cd financial_marketing_analyzer
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the Model

```
python src/train_model.py
```

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

##  Features

* ✔ Customer Purchase Prediction
* ✔ Customer Segmentation (K-Means Clustering)
* ✔ AI-based Marketing Insights
* ✔ Interactive Dashboard
* ✔ API Support (FastAPI)

---

##  How It Works

1. Data is collected and preprocessed
2. Machine Learning models are trained
3. Predictions and segmentation are performed
4. AI generates insights based on results
5. Results are displayed in a dashboard

---

##  Output Example

* Prediction: **Will Buy / Will Not Buy**
* Segment: **High / Medium / Low Value Customer**
* AI Insight: Personalized marketing recommendation

---

##  Security Note

* API keys are **NOT included** in this repository
* Use a `.env` file to store sensitive information

Example:

```
OPENAI_API_KEY=your_api_key_here
```

---

##  Project Report

 You can view the full report here:
👉 `report/project_report.pdf`

---

##  Future Enhancements

* Real-time data integration
* Advanced ML models (Random Forest, XGBoost)
* Deployment as a web application
* Chatbot integration

---

## 👨 Author

**AVVARU UJWAL **

* BTech CSE Student
* Aspiring AI/ML Developer

---

##  Conclusion

This project demonstrates the integration of **Machine Learning and Generative AI** to solve real-world financial marketing problems effectively.

---

##  If you like this project

Give it a ⭐ on GitHub!
