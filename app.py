import streamlit as st
from predict_page import show_predict_page

st.set_page_config(page_title="Salary Prediction App")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Predict Salary",))

if page == "Predict Salary":
    show_predict_page()