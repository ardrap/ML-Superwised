# -*- coding: utf-8 -*-
"""startup_RF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sbynVEPlr14uahyXwZdTUw74SVsUn2Qe
"""

import pandas as pd
import numpy as np
df=pd.read_csv("https://raw.githubusercontent.com/arib168/data/main/50_Startups.csv")
df.head()

# convert object into neumerical value
from sklearn.preprocessing import LabelEncoder
coder=LabelEncoder()
df['State']=coder.fit_transform(df['State'])
df

#input and output
x=df.iloc[:,:-1].values
x

y=df.iloc[:,-1].values
y

# convert it to training data and testing data/model selection
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
x_train
x_test
y_train
y_test

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=3)
reg.fit(x_train,y_train)

y_pred=reg.predict(x_test)
y_pred

from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error,mean_squared_error
print('MAE',mean_absolute_error(y_test,y_pred))
print('EP',mean_absolute_percentage_error(y_test,y_pred))
print('accuracy',1-mean_absolute_percentage_error(y_test,y_pred))
print('MSE',mean_squared_error(y_test,y_pred))
print('RMSE',np.sqrt(mean_squared_error(y_test,y_pred)))

"""score=accuracy_score(y_test,y_pred)
print(score)
"""

