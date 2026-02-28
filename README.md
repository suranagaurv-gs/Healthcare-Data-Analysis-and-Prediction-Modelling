#  Healthcare Stroke Prediction Project

---

##  Project Overview

This project focuses on analyzing a healthcare dataset and building machine learning models to predict the likelihood of stroke occurrence.

Stroke is one of the leading causes of death and disability worldwide. Early detection can significantly improve treatment outcomes. This project applies data science techniques to develop an accurate, interpretable, and deployable stroke prediction system.

The final output includes a trained machine learning model integrated into a Streamlit web application for real-time prediction.

---

##  Objectives

- Perform Exploratory Data Analysis (EDA)
- Handle missing values and categorical variables
- Address class imbalance using SMOTE
- Build and compare classification models
- Evaluate performance using appropriate metrics
- Perform hyperparameter tuning
- Deploy the trained model using a Streamlit Web App

---

#  Project Structure

project/
│
├── notebooks/
│   ├── Comprehensive EDA and Data Preparation for Healthcare Data (Stroke Prediction).ipynb
│   └── Predictive Model Building and Evaluation (Stroke Prediction).ipynb
│
├── data/
│   ├── original/
│   └── processed/
│
├── models/
│   ├── model.pkl
│   └── columns.pkl
│
├── app/
│   └── app.py
│
├── requirements.txt
└── README.md


---

#  Exploratory Data Analysis (EDA)

The following analysis was performed:

- Dataset inspection and summary statistics
- Missing value detection and handling
- Age distribution visualization
- BMI and glucose level analysis
- Correlation heatmap
- Target variable distribution (Stroke vs No Stroke)

EDA helped understand feature relationships and class imbalance.

---

#  Data Preprocessing

- Missing values handled using mean imputation (BMI)
- Categorical variables encoded using:
  - Label Encoding (Binary variables)
  - One-Hot Encoding (Multi-class variables)
- Feature scaling using StandardScaler
- Train-test split (80:20 ratio)

A consistent preprocessing pipeline (ColumnTransformer) was created and saved for use in the web application.

---

#  Handling Imbalanced Data

Since stroke cases were underrepresented:

- SMOTE (Synthetic Minority Oversampling Technique)
- Class weighting in models
- Focus on Recall and F1-score

Improving Recall was prioritized to reduce false negatives.

---

#  Models Implemented

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting (Optional)

Random Forest provided the best performance after hyperparameter tuning.

---

#  Model Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Special emphasis was placed on **Recall**, as missing a stroke case can have serious consequences.

---

#  Analysis of Feature Dominance

Insight: The feature class_Economy accounts for the vast majority of the model's predictive power.

The Challenge: Because the price gap between Economy and Business is so massive (e.g., $5,000 vs $50,000), the model prioritizes this distinction above all else.

The Result: Factors like 'Time of Departure' or 'Source City' show lower importance globally, even though they significantly affect prices within the Economy class specifically.

---

#  Hyperparameter Tuning

- GridSearchCV
- RandomizedSearchCV
- Optimization of:
  - n_estimators
  - max_depth
  - min_samples_split

---

#  Web Application (Streamlit)

A Streamlit web app was developed to allow real-time stroke prediction.

###  Features

- User-friendly interface
- Input fields for:
  - Age
  - Gender
  - Hypertension
  - Heart Disease
  - Ever Married
  - Work Type
  - Residence Type
  - Average Glucose Level
  - BMI
  - Smoking Status
- Loads saved trained model (`model.pkl`)
- Loads preprocessing pipeline (`preprocessor.pkl`)
- Applies the same preprocessing used during training
- Generates instant stroke prediction
- Displays result clearly as:
  -  No Stroke
  -  High Stroke Risk

---

#  Model Serialization

The trained model and preprocessing pipeline were saved using:

- joblib / pickle
- Ensured feature names match training data
- Integrated directly into the Streamlit app

---

