import matlab.engine
import numpy as np
import pandas as pd

engine = matlab.engine.start_matlab()
data = engine.load("./matlab/asherTrial2.mat")

position = data["Position"]
latitude = np.array(engine.getfield(position, "latitude"))
longitude = np.array(engine.getfield(position, "longitude"))
speed = np.array(engine.getfield(position, "speed"))