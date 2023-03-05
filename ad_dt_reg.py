# -*- coding: utf-8 -*-
"""Ad_DT_reg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VJcVOR_slKCND-PpCNXmPqoPRfixVQs5
"""

import numpy as np
import pandas as pd
import seaborn as sns
df=pd.read_csv("/content/Advertising.csv")
df

df.describe()

print(df.isna().sum())

# input and output
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values
print(x)
print(y)

df.columns

# model_selection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)
x_train
x_test
y_train
y_test

# pre-processing
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x_train)

x_train=scaler.transform(x_train)
x_train

x_test=scaler.transform(x_test)
x_test

from sklearn.tree import DecisionTreeRegressor 
classifier=DecisionTreeRegressor()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
y_pred

# Mean Absolute Error
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error
print("Mean Absolute Error is",mean_absolute_error(y_test,y_pred))
print("Error Precentage",mean_absolute_percentage_error(y_test,y_pred))

# Mean Squared Error
from sklearn.metrics import mean_squared_error,mean_squared_log_error
print("MSE",mean_squared_error(y_test,y_pred))

# Root Mean Squared
print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))