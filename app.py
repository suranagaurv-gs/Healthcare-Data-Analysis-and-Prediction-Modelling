import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
columns = joblib.load("models/columns.pkl")

st.title("Stroke Prediction Web App")

# ================= INPUTS =================

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 1, 120)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type",
                         ["Private", "Self-employed",
                          "Govt_job", "children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level")
bmi = st.number_input("BMI")
smoking_status = st.selectbox("Smoking Status",
                              ["formerly smoked", "never smoked", "smokes"])

# ================= PREDICT =================

if st.button("Predict"):

    # Create full zero dictionary
    input_dict = dict.fromkeys(columns, 0)

    # ID (since model expects it)
    input_dict["id"] = 0   # dummy value

    # Numeric columns
    input_dict["age"] = age
    input_dict["hypertension"] = hypertension
    input_dict["heart_disease"] = heart_disease
    input_dict["avg_glucose_level"] = avg_glucose_level
    input_dict["bmi"] = bmi

    # Binary columns (NOT one-hot)
    input_dict["gender"] = 1 if gender == "Male" else 0
    input_dict["ever_married"] = 1 if ever_married == "Yes" else 0

    # One-hot columns
    if f"work_type_{work_type}" in input_dict:
        input_dict[f"work_type_{work_type}"] = 1

    if Residence_type == "Urban":
        input_dict["Residence_type_Urban"] = 1

    if f"smoking_status_{smoking_status}" in input_dict:
        input_dict[f"smoking_status_{smoking_status}"] = 1

    input_data = pd.DataFrame([input_dict])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Stroke")
    else:
        st.success("Low Risk of Stroke")