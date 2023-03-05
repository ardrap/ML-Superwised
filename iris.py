# -*- coding: utf-8 -*-
"""Iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19qsAUbPSHHdYpAyzVqmvIkDaTd9nnCHP
"""

from sklearn.metrics._plot.confusion_matrix import ConfusionMatrixDisplay
import numpy as np
import pandas as pd

df=pd.read_csv('/content/Iris.csv')
print(df)

df.shape

df.describe()

print(df.isna().sum())
# df1=df.groupby('Species') ['Species'].count()
# print(df1)

df['Species'].value_counts()

df1=df.drop(['Id'],axis=1)
print(df1)

#input and output
x=df1.iloc[:,:-1].values
y=df1.iloc[:,-1].values
print(x)
print("="*100)
print(y)

# convert it to training data and testing data/model selection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30)
print(x_train)
print("="*100)
print(x_test)
print("="*100)
print(y_train)
print("="*100)
print(y_test)
print("="*100)

# pre-processing
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x_train)

x_train=scaler.transform(x_train)
print(x_train)
print("="*50)
x_test=scaler.transform(x_test)
print(x_test)

# model creation
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=7)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(y_pred)

# confusion matrix and confusion matrix display
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,ConfusionMatrixDisplay
labels=['Iris-versicolor','Iris-setosa','Iris-virginica']
result=confusion_matrix(y_test,y_pred)
print(result)

cmd=ConfusionMatrixDisplay(result,display_labels=labels)
cmd.plot()

score=accuracy_score(y_test,y_pred)
print(score)