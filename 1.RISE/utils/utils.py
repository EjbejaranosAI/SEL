from sqlite3 import Row
import numpy as np

import pandas as pd
import seaborn as sns
import matplotlib as plt
import glob, os



def load_datasets(path_dataset):
    array = glob.glob(os.path.join(path_dataset, '*.csv'))

    df = []
    df_small = []
    df_middle = []
    df_big = []

    for i in range(len(array)):
        df = pd.read_csv(array[i])
        df = pd.DataFrame(df)
        if df.shape[0] < 500:
            df_small.append(df)
        elif df.shape[0] > 500 and df.shape[0] < 2000:
            df_middle.append(df)
        elif df.shape[0] > 2000 and df.shape[0]:
            df_big.append(df)
        else:
            print('Error')
        print("Dataset: ", array[i],"\n", "Shape: ", df.shape, "\n")
        EDA_dataset(df)        
    return(df_small, df_middle, df_big)


def EDA_dataset(df):
    print(f'The shape of the dataset is: {df.shape}')
    print(f'The unique value is:\n{df.nunique()}')
    print(f'The number of missing values is:\n{df.isnull().sum()}')
    print(f'The number of duplicates is: {df.duplicated().sum()}')
    print(f'Head of the dataset:\n{df.head(10)}')
    

def correlation(df):
    correlation = df.corr()
    sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns)
    