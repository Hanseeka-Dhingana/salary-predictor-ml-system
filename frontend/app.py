import streamlit as st
import requests


# Config
API_URL = "https://salary-predictor-api-production.up.railway.app/predict"  


# App Title
st.title("Salary Predictor")
st.write("Predict your salary based on years of experience")


# User Input
experience = st.number_input("Enter your years of experience", min_value=0.0, max_value=50.0, value=1.0, step=0.1)


# Predict Button
if st.button("Predict Salary"):
    payload = {"experience_years": experience}
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            salary = data.get("predicted_salary")
            st.success(f"💰 Predicted Salary: ${salary:,.2f}")
        else:
            st.error(f"Error from API: {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")