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

name_datasets("../databases")
