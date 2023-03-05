# -*- coding: utf-8 -*-
"""house_mul.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gWveiSipZpopKJz4KdFdquUiwc0IbpV3
"""

import numpy as np
import pandas as pd
df=pd.read_csv("/content/kc_house_data.csv")
print(df)

df.head

df.describe()

df.columns

print(df.isna().sum())

df1=df.drop(['id','date','zipcode'],axis=1)
print(df1)

print(df1.isna().sum())

# categorical data display
categorical=[var for var in df1.columns if df1[var].dtype=='O']
print("Categorical variables are",categorical)

# count of categorical data
for var in categorical:
  print(df1[var].value_counts())

# null value in categorical data
df[categorical].isnull().sum()

# input and output
x=df1.iloc[:,:-1].values
y=df1.iloc[:,-1].values
print(x)
print(y)

# model selection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

# pre-processing
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x_train)

x_train=scaler.transform(x_train)
print(x_train)
x_test=scaler.transform(x_test)
print(x_test)

# model creation
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,y_train)

y_pred=reg.predict(x_test)
print(y_pred)

print("intercept",reg.intercept_)

df_pred=pd.DataFrame({'Actual value':y_test,'Predicted value':y_pred})
print(df_pred)

# MAE
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error
print("MAE",mean_absolute_error(y_test,y_pred))
print("MAEP",mean_absolute_percentage_error(y_test,y_pred))
print('accuracy',1-mean_absolute_percentage_error(y_test,y_pred))

# Mean Squared Error
from sklearn.metrics import mean_squared_error,mean_squared_log_error
print("MSE",mean_squared_error(y_test,y_pred))

# Root Mean Squared
print("RMSE",np.sqrt(mean_squared_error(y_test,y_pred)))