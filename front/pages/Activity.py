import matlab.engine
import numpy as np
import pandas as pd
import streamlit as st
import joblib
import UserInfo as ui


@st.cache_data
def load_matlab_data():
    engine = matlab.engine.start_matlab()
    data = engine.load("front/pages/trial1.mat")

    acceleration = data["Acceleration"]
    x = np.array(engine.getfield(acceleration, "X"))
    y = np.array(engine.getfield(acceleration, "Y"))
    z = np.array(engine.getfield(acceleration, "Z"))

    positions = data["Position"]
    speeds = np.array(engine.getfield(positions, "speed"))

    df_X = pd.DataFrame(x)
    df_Y = pd.DataFrame(y)
    df_Z = pd.DataFrame(z)

    return df_X, df_Y, df_Z, speeds


model = joblib.load("front/pages/hack_uta_mod.joblib")
X, Y, Z, speed = load_matlab_data()


@st.cache_data
def load_prediction_data():
    df = pd.concat([X, Y, Z], axis=1)
    predictions = model.predict(df)
    index = np.argmax(predictions)

    walk = 0
    climb = 0
    run = 0
    if predictions[index] == 0:
        walk += 1
    elif predictions[index] == 1:
        climb += 1
    elif predictions[index] == 2:
        run += 1
    
    prediction = ""
    if (walk >= climb) and (walk >= run):
        prediction = "walking"
    elif (climb >= walk) and (climb >= run):
        prediction = "climbing"
    else:
        prediction = "running"
    
    return prediction


prediction = load_prediction_data()
calories = 

st.title("Activity")
st.write("The user is currently", prediction,".")
st.line_chart(speed)

st.header("Calories burned in an hour of activity:")

