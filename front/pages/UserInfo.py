import streamlit as st

#Asks the user about their biological sex, age, weight, and height
st.header("User info:")
sex = st.radio("Sex:",["Male", "Female"])
age = st.number_input("Age:", 1, 110)
weight = st.number_input("Weight in lbs:", 50,500)
height = st.number_input("Height in inches:", 4.00,7.00)