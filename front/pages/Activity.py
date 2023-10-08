import matlab.engine
import numpy as np
import pandas as pd
import streamlit as st
import joblib

model = joblib.load("filename")

@st.cache_data
def load_matlab_data():
    engine = matlab.engine.start_matlab()
    data = engine.load("C:/Users/asher/Desktop/Programs/VSCode/HackUTA/hack-uta-2023/front/pages/asherTrial2.mat")
    
    position = data["Position"]
    latitude = np.array(engine.getfield(position, "latitude"))
    longitude = np.array(engine.getfield(position, "longitude"))
    speed = np.array(engine.getfield(position, "speed"))

    return latitude, longitude, speed

latitude, longitude, speed = load_matlab_data()

st.title("Activity")
st.line_chart(speed)
