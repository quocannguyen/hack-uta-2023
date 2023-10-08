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
MET = 0
if prediction == "walking":
    MET = 2.5
elif prediction == "climbing":
    MET = 4
elif prediction == "running":
    MET = 10


# calories = st.session_state.weight * MET

st.title("Activity")
st.write("The user is currently", prediction, ".")
st.line_chart(speed)

st.header("Calories burned in an hour of activity:")
if "weight" in st.session_state:
    x = st.session_state.weight * MET
    st.write(x)
    activity_mult = x = st.session_state.weight * MET * .5
    if (x > activity_mult):
        st.write(
            "Good Workout. You beat a 12-minute pace record of burning more than 314 calories")
    elif (x > activity_mult):
        st.write("Solid effort!! 10 minute-pace record seems way easy for you!")
    elif (x > activity_mult):
        st.write(
            "Brilliant!!! You burned more calories than an average human weighing around 70 kilograms! ")
    else:
        st.write(
            "No worries if you scored low! Everyone has to start at the bottom! Way to go")
