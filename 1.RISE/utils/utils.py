import numpy as np

import pandas as pd
import seaborn as sns
import matplotlib as plt
import glob, os


origin_path = r"../1.RISE/databases"


def name_datasets(path_datasets):
    name_datasets = []
    os.chdir(path_datasets)
    for file in glob.glob("*.data"):
        name_datasets.append(file)
    print(f"You find {len(name_datasets)} datasets")
    return name_datasets

def load_dataset(path,name_path,columns_name):
    df = []
    df = pd.read_csv(path+'/'+name_path)
    df.columns = columns_name
    df.head(5)

    return df

columns_name_wine = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']

nm_data = name_datasets("../databases")
df = load_dataset("../databases",nm_data[0],columns_name_wine)
print(df.head(5))
print(df.unique())


