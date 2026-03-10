# 🏠 Ames Housing Price Prediction

## 📌 Project Overview

This project predicts house sale prices using the Ames Housing dataset from Kaggle.
The model uses machine learning techniques such as feature engineering and Linear Regression to estimate house prices based on property characteristics.

Dataset Source: Kaggle – House Prices: Advanced Regression Techniques

---

## 🎯 Problem Statement

Predict the sale price of houses using various property features such as living area, garage capacity, and overall quality.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 🧠 Machine Learning Workflow

1. Data Loading
2. Handling Missing Values
3. Feature Engineering
4. Model Training using Linear Regression
5. Model Evaluation

---

## 🛠 Feature Engineering

Two new features were created:

**Total Area**

Total Area = Basement Area + 1st Floor Area + 2nd Floor Area

**House Age**

House Age = Current Year − Year Built

---

## 📊 Model Evaluation

Metrics used:

* RMSE (Root Mean Squared Error)
* R² Score

These metrics measure how accurately the model predicts house prices.

---

## 🌐 Streamlit Web Application

A Streamlit web application was created to allow users to input house features and predict the sale price dynamically.

To run locally:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

house_price_prediction
│
├── app.py
├── housing_model.ipynb
├── house_price_model.pkl
├── train.csv
├── test.csv
├── requirements.txt
└── README.md

---

## 🚀 Future Improvements

* Use advanced models like Random Forest or XGBoost
* Improve feature selection
* Enhance the web interface
