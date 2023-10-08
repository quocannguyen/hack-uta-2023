import matlab.engine
import numpy as np
import pandas as pd
# import matlab
# "C:/Users/nishi/MATLAB Drive/MobileSensorData/sensorlog_20231007_164048.mat"

engine = matlab.engine.start_matlab()
data = engine.load(
    "C:/Users/nishi/MATLAB Drive/MobileSensorData/asherTrial2.mat")

position = data["Position"]
latitude = np.array(engine.getfield(position, "latitude"))
longitude = np.array(engine.getfield(position, "longitude"))
speed = np.array(engine.getfield(position, "speed"))
