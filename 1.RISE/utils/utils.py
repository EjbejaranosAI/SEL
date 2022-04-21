from sqlite3 import Row
import numpy as np

import pandas as pd
import seaborn as sns
import matplotlib as plt
import glob, os




def get_path_dataset(path):
    name_datasets = []
    for file in glob.glob(path):
        name_datasets.append(file)

    df = []
    for i in range(len(name_datasets)):
        df[i].append(pd.read_csv(name_datasets[i]))
    #df = pd.DataFrame(df)
    return df
