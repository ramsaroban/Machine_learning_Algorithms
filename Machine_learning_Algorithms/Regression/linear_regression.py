"""
Chapter 1.1
Author: Ram Saroban Kumar Das
Desc: Linear regression model on weather data
"""
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstances

from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#%matplotlib inline

#Load Dataset
dataset = pd.read_csv("Weather.csv")
#print(dataset.shape)
#print(dataset.describe())
dataset.plot(x='MinTemp',y='MaxTemp',style='o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()
#plt.savefig("MinTemp_MaxTemp.png")