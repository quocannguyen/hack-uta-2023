import matlab.engine
import numpy as np
import pandas as pd
import streamlit as st
import joblib


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

    prediction = ""
    if predictions[index] == 0:
        prediction = "Walk"
    elif predictions[index] == 1:
        prediction = "Climb"
    elif predictions[index] == 2:
        prediction = "Run"

    return prediction


prediction = load_prediction_data()

st.title("Activity")
st.line_chart(speed)

st.text(prediction)
