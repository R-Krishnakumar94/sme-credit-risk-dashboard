
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

