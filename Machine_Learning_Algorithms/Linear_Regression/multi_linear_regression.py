# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 01:40:26 2025

@author: gjrah
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\gjrah\Documents\Data Science\Data_Science\Machine_Learning_Algorithms\Linear_Regression\homeprices.csv")

#Display the data
df.head()

#Summarize the null values
df.isnull().sum()

#Bedroom has one null value

#Let's try to find out the meadian value

bedroom_median = np.median(df['bedroom'])