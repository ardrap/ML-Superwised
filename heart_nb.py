# -*- coding: utf-8 -*-
"""heart_NB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15kdkaD6DxT3sMJrnEmCvDe3ZbMITFkM1
"""

import numpy as np
import pandas as pd
df=pd.read_csv("/content/heart.csv")
print(df)
print(df.isna().sum())
df['target'].value_counts()
df.describe()

# input and output
x=df.iloc[:,:-1].values
print(x)
y=df.iloc[:,-1].values
print(y)

# model_seleection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


# pre-processing / transsform
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

x_train=scaler.fit_transform(x_train)
print(x_train)
x_test=scaler.fit_transform(x_test)
print(x_test)

# model creation
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)

# accuracy
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
result=confusion_matrix(y_pred,y_test)
print(result)

score=accuracy_score(y_pred,y_test)
print(score)