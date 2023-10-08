import pandas as pd
import numpy as np


def get_df():
    position_file_names = [
        "position_climb_1.txt",
        "position_climb_2.txt",
        "position_climb_3.txt",
        "position_climb_4.txt",
        "position_climb_5.txt",
        "position_run_1.txt",
        "position_run_2.txt",
        "position_walk_1.txt",
        "position_walk_2.txt",
        "position_walk_3.txt",
        "position_walk_4.txt",
        "position_walk_5.txt",
        "position_walk_6.txt",
    ]
    climb_acceleration = ["acceleration_climb_1.txt",
                          "acceleration_climb_2.txt",
                          "acceleration_climb_3.txt",
                          "acceleration_climb_4.txt",
                          "acceleration_climb_5.txt"]

    run_acceleration = ["acceleration_run_1.txt",
                        "acceleration_run_2.txt"]

    walk_acceleration_file_names = [
        "acceleration_walk_1.txt",
        "acceleration_walk_2.txt",
        "acceleration_walk_3.txt",
        "acceleration_walk_4.txt",
        "acceleration_walk_5.txt",
        "acceleration_walk_6.txt",
    ]

    file_path = "./data/" + position_file_names[0]
    df_position = pd.read_csv(file_path)
    for i in range(1, len(position_file_names)):
        file_path = "./data/" + position_file_names[i]
        new_df_position = pd.read_csv(file_path)
        df_position = pd.concat([new_df_position, df_position])

    file_path = "./data/" + walk_acceleration_file_names[0]

    df_walk_acceleration = pd.read_csv(file_path)
    for i in range(1, len(walk_acceleration_file_names)):
        file_path = "./data/" + walk_acceleration_file_names[i]
        new_df_acceleration = pd.read_csv(file_path)
        df1 = pd.concat([new_df_acceleration, df_walk_acceleration])
        df1['target'] = 0

    file_path = "./data/" + climb_acceleration[0]
    df_climb_acceleration = pd.read_csv(file_path)
    for i in range(1, len(climb_acceleration)):
        file_path = "./data/" + climb_acceleration[i]
        new_df_acceleration = pd.read_csv(file_path)
        df2 = pd.concat([new_df_acceleration, df_climb_acceleration])
        df2['target'] = 1

    file_path = "./data/" + run_acceleration[0]
    df_run_acceleration = pd.read_csv(file_path)
    for i in range(1, 2):
        file_path = "./data/" + run_acceleration[i]
        new_df_acceleration = pd.read_csv(file_path)
        df3 = pd.concat([new_df_acceleration, df_run_acceleration])
        df3['target'] = 2

    df = pd.concat([df1, df2, df3]).reset_index(drop=True)

    df = df.drop(['Timestamp'], axis=1)

    return df
