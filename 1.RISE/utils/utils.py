from sqlite3 import Row
import numpy as np

import pandas as pd
import seaborn as sns
import matplotlib as plt
import glob, os


origin_path = r"../1.RISE/databases"


def name_datasets(path_datasets):
    name_datasets = []
    os.chdir(path_datasets)
    for file in glob.glob("*.xlsx"):
        name_datasets.append(file)

    for file in glob.glob("*.data"):
        name_datasets.append(file)

    print(f"You find {len(name_datasets)} datasets")
    return name_datasets

def read_dataset(path,name_path):
    df = []
    df = pd.read_csv(path+'/'+name_path)
    #df.columns = columns_name
    return df



    
columns_name_wine = ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
columns_name_adult = ["target","age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country"]
columns_name_cmc = ["Wife's age","Wife's education","Husband's education",'Number of children ever born',"Wife's religion","Wife's now working?","Wife's now working?","Husband's occupation",'Standard-of-living index','Media exposure','Contraceptive method used']

columns_name = [columns_name_wine,columns_name_adult,columns_name_cmc]
nm_data = name_datasets("../databases")
print(f"The datasets that you contain are: {nm_data}")

def load_datasets(name_files):


    df = []
    df_small = []
    df_med = []
    df_big = []

    for i in range(len(name_files)):
        df.append(read_dataset("../databases",name_files[i])) 
        if len(df[i])>2000:
            df_big = df[i]
            
        elif len(df[i])>500<2000:
            df_med = df[i]
            
        elif len(df[i])<500:
            df_small = df[i]
        else:
            print("Fuera de los rangos")

    print(f"The small dataset contain : {len(df_small)} instances")
    print(f"The medium dataset contain : {len(df_med)} instances")
    print(f"The big dataset contain : {len(df_big)} instances")
    
    return df, df_big,df_med,df_small

allData, df_big,df_med,df_small = load_datasets(nm_data)

def add_columns(dataset,name_column):
    dataset.columns = name_column
    return dataset


'''df_small = add_columns(df_small,columns_name_wine)
#df_med = add_columns(df_med,columns_name_cmc)
df_big = add_columns(df_big,columns_name_adult)


'''
print(df_med.head())

print(np.shape(df_big))
print(len(columns_name_adult))
print(np.shape(df_small))
print(len(columns_name_wine))
print(np.shape(df_med))
print(len(columns_name_cmc))


'''df_big.columns = columns_name_adult     
df_med.columns = columns_name_cmc
df_small.columns = columns_name_wine'''