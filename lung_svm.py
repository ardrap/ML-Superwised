# -*- coding: utf-8 -*-
"""lung_SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CZeVkEeckMhmoXqeCPgdW7vdsclYkSff
"""

from pandas.core.common import random_state
import pandas as pd
import numpy as np
df=pd.read_csv("/content/lung_cancer_examples.csv")
# print(df)
print(df.isna().sum())
df.describe()
df['Result'].value_counts()

# input and output
x=df.iloc[:,2:6].values
print(x)
y=df.iloc[:,-1].values
print(y)

# model selection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

# pre-processing/transform
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# scaler.fit(x_train)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(x_train)
scaler.fit(x_test)

x_train=scaler.transform(x_train)
print(x_train)
x_test=scaler.transform(x_test)
print(x_test)

# model creation
from sklearn.svm import SVC
classifier=SVC()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)

# acccuracy
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
result=confusion_matrix(y_pred,y_test)
print(result)

score=accuracy_score(y_pred,y_test)
print(score)