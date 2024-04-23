import streamlit as st
import pickle
import numpy as np

def load_model(file_path='saved_steps.pkl'):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def predict_salary(country, education_level, experience_years, file_path='saved_steps.pkl'):
    data = load_model(file_path)
    regressor = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]
    
    # Pre-process input data
    X = np.array([[country, education_level, experience_years]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)
    
    # Make prediction
    salary = regressor.predict(X)
    return salary[0]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States", "India", "United Kingdom", "Germany", "Canada",
        "Brazil", "France", "Spain", "Australia", "Netherlands", "Poland",
        "Italy", "Russian Federation", "Sweden"
    )

    education = (
        "Less than a Bachelors", "Bachelor’s degree", "Master’s degree", "Post grad"
    )

    country = st.selectbox("Country", countries)
    education_level = st.selectbox("Education Level", education)
    experience_years = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        salary = predict_salary(country, education_level, experience_years)
        st.subheader(f"The estimated salary is ${salary:.2f}")
