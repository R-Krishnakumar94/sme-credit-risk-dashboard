# 💳 SME Credit Risk Scoring Dashboard

An AI-powered credit risk scoring dashboard designed for **small and medium-sized enterprises (SMEs)**. This Streamlit app enables banks, fintech companies, and lenders to assess the risk level of SMEs using key financial and behavioral indicators.

🔗 **Live App**: [http://bit.ly/45EmzRz](http://bit.ly/45EmzRz)  
📦 **Model**: Trained using XGBoost on synthetic SME financial data  
📊 **Dashboard**: Built with Streamlit + Python  
📁 **Status**: MVP complete, ready for further integration or API deployment

---

## 🧾 Introduction to SME Credit Risk Scoring

**Credit Risk Score** is a numerical estimation of the likelihood that a borrower (in this case, an SME) will default on a loan. Unlike large corporations, **SMEs (Small and Medium Enterprises)** often lack detailed credit histories, making them harder to assess using traditional scoring methods.

This web application solves that problem by allowing banks, NBFCs, and fintech lenders to upload SME financial data in Excel format, and instantly get a machine learning–powered **credit risk score**.

The app is ideal for:
- Commercial banks and lending institutions
- NBFCs offering SME loans
- Government-backed microfinance or startup funding bodies
- Fintech platforms offering invoice financing, BNPL, or credit lines

---

## 🧮 How the Credit Risk Score Is Calculated

The risk score is calculated using an **XGBoost machine learning model** trained on synthetic SME financial data. The model looks at features such as:

- Monthly income and expenses
- Net profit margin
- Loan size requested
- Growth rate in revenue
- Timeliness of previous payments
- Dependency on vendors
- Business age and size

From this, the model classifies the SME into:
- `✅ Low Risk`: Likely to repay loan on time
- `❗ High Risk`: May default or delay payments

---

## 🔍 What the Risk Score Means

- **High Risk (❗)**: The SME has financial behavior patterns or business signals that indicate elevated default probability. Lenders should review manually or request additional documentation before approving a loan.
- **Low Risk (✅)**: The SME appears financially sound based on submitted data. May be eligible for faster or pre-approved credit.

---

## 📥 Required Data for Risk Scoring

To generate a credit risk score, the SME applying for a loan should provide the following data in an Excel file:

| Column Name | Description |
|-------------|-------------|
| `monthly_income` | Average monthly revenue |
| `monthly_expense` | Monthly operational or recurring costs |
| `net_profit_margin` | Profitability as a % of revenue (e.g., 0.25 = 25%) |
| `missed_payments_last_6m` | Number of missed bills, EMIs, or invoices in the past 6 months |
| `years_in_business` | How long the SME has operated |
| `num_employees` | Number of staff or team members |
| `vendor_concentration_ratio` | % of business reliant on top 1-2 vendors (0.1–0.9 scale) |
| `invoice_paid_on_time_rate` | % of customer invoices paid on time |
| `loan_amount_requested` | Size of loan the SME is applying for |
| `revenue_growth_rate` | Revenue change over the last few months (negative or positive) |

The model will then compute additional internal features and generate the final credit risk prediction.

---


# 💳 SME Credit Risk Scoring Dashboard

An AI-powered credit risk scoring dashboard designed for **small and medium-sized enterprises (SMEs)**. This Streamlit app enables banks, fintech companies, and lenders to assess the risk level of SMEs using key financial and behavioral indicators.

🔗 **Live App**: [http://bit.ly/45EmzRz](http://bit.ly/45EmzRz)  
📦 **Model**: Trained using XGBoost on synthetic SME financial data  
📊 **Dashboard**: Built with Streamlit + Python  
📁 **Status**: MVP complete, ready for further integration or API deployment

---

## 📌 Table of Contents

- [🎯 Problem Statement](#-problem-statement)
- [🚀 Project Objectives](#-project-objectives)
- [📊 Features](#-features)
- [🧠 Model Details](#-model-details)
- [🧾 Dataset Description](#-dataset-description)
- [💻 How to Run This App](#-how-to-run-this-app)
- [📸 Preview](#-preview)
- [🛠 Tech Stack](#-tech-stack)
- [🧑‍💼 Use Cases](#-use-cases)
- [📈 Future Enhancements](#-future-enhancements)
- [📬 Contact](#-contact)

---

## 🎯 Problem Statement

Traditional credit scoring systems struggle with evaluating **SMEs**, especially those without a long credit history ("thin file" problem). Many lenders rely on manual assessments, which are slow, inconsistent, and not scalable.

---

## 🚀 Project Objectives

- Simulate a realistic SME financial dataset
- Train a machine learning model to predict SME credit risk
- Build an interactive web dashboard for:
  - Uploading SME data
  - Predicting risk categories
  - Visualizing risk summaries
- Make the app accessible online via Streamlit Cloud

---

## 📊 Features

- 🧾 Upload SME financial data (Excel `.xlsx`)
- 🤖 Predict SME risk as `✅ Low Risk` or `❗ High Risk`
- 📊 Visualize overall risk distribution with dynamic bar chart
- 🔎 Filter and review high-risk SMEs in a clean table
- 📁 Downloadable and easy to integrate into further workflows

---

## 🧠 Model Details

- Algorithm: `XGBoost Classifier`
- Target Variable: `risk_label` (0 = Low Risk, 1 = High Risk)
- Performance:
  - Accuracy: **99.5%**
  - Precision/Recall: Excellent recall for high-risk class
- Model saved using `joblib` for deployment in Streamlit

---

## 🧾 Dataset Description

Synthetic dataset of **1,000 SME records** with the following fields:

| Column                     | Description |
|----------------------------|-------------|
| `monthly_income`           | Monthly revenue in INR |
| `monthly_expense`          | Total operating cost |
| `net_profit_margin`        | Profit as a % of income |
| `missed_payments_last_6m`  | Count of late utility/invoice payments |
| `years_in_business`        | Business age |
| `vendor_concentration_ratio` | Risk of supply chain dependency |
| `invoice_paid_on_time_rate` | Reliability score |
| `loan_amount_requested`    | Requested loan size |
| `revenue_growth_rate`      | Recent trend in revenue |
| `risk_label`               | Actual credit risk (simulated) |
| ➕ Engineered features: `profit_amount`, `debt_to_income_ratio`, `cash_flow_stability`

---

## 💻 How to Run This App Locally

### 1. Clone the repository:

```bash
git clone https://github.com/R-Krishnakumar94/sme-credit-risk-dashboard.git
cd sme-credit-risk-dashboard
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app:

```bash
streamlit run credit_app.py
```

Make sure the model file `xgb_credit_model.pkl` is in the same folder.

---

## 📸 Preview
![screenshot-2](screenshot-2.png)
![screenshot-3](screenshot-3.png)



---

## 🛠 Tech Stack

- Python 3.x
- Streamlit
- XGBoost
- Pandas, NumPy
- scikit-learn
- joblib
- Excel (`.xlsx`) as input

---

## 🧑‍💼 Use Cases

- Credit assessment for MSMEs by banks or NBFCs
- Fintech loan approval platforms
- Government-backed microfinance scoring tools
- Financial inclusion analytics
- Risk-as-a-Service prototype for small business lending

---

## 📈 Future Enhancements

- ✅ SHAP-based explainability (why a business is risky)
- ✅ PDF report generator per SME
- ✅ Upload multiple files / batch processing
- ✅ API deployment using FastAPI
- ✅ Authentication for secured use

---

## 📬 Contact

**Rakesh Krishna Kumar**  
📧 rakesh.krishee@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rakesh-krishna-kumar)  
💼 [GitHub](https://github.com/R-Krishnakumar94)
