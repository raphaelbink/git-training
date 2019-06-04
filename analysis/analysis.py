import pandas as pd
import numpy as np
import sklearn as sk

data = pd.read_csv('../data/factory_data.csv')

print(data.describe())
print(data.shape)
print(data['humidity'].corr(data['linespeed']))

print("hi there")
