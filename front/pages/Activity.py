import matlab.engine
import numpy as np
import pandas as pd
import streamlit as st
import joblib

@st.cache_data
def load_matlab_data():
    engine = matlab.engine.start_matlab()
    data = engine.load("trial1.mat")
    
    acceleration = data["Acceleration"]
    x = np.array(engine.getfield(acceleration, "X"))
    y = np.array(engine.getfield(acceleration, "Y"))
    z = np.array(engine.getfield(acceleration, "Z"))

    df_X = pd.DataFrame(x)
    df_Y = pd.DataFrame(y)
    df_Z = pd.DataFrame(z)

    return df_X, df_Y, df_Z

model = joblib.load("hack_uta_mod.joblib")
X, Y, Z = load_matlab_data()

df = pd.concat([X, Y, Z], axis=1)
print(df)

print(model.predict(df))
#st.title("Activity")
#st.line_chart(speed)
