'''----RISE CLASSIFIER - Author: Edison Jair Bejarano Sepulveda----'''

#Import libraries
import pandas as pd
import numpy as np
import glob, os
import seaborn as sns
import matplotlib.pyplot as plt


#%pip install reload_ext autoreload

#import own libraries
from utils.utils import load_datasets, EDA_dataset, correlation


#Load datasets
path_dataset = "./data/"
small, middle, big = load_datasets(path_dataset) 


print(small[0].shape)
print(middle[0].shape)
print(big[0].shape)