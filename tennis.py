# -*- coding: utf-8 -*-
"""Tennis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fnheugqeXXBLtqSOnnaavcwjuGCPSdKE
"""

Outlook=['sunny','sunny','overcast','rain','rain','rain','overcast','sunny','sunny','rain','sunny','overcast','overcast','rain']
Temperature=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
Humidity=['high','high','high','high','normal','normal','normal','high','normal','normal','normal','high','normal','high']
Wind=['weak','strong','weak','weak','weak','strong','strong','weak','weak','weak','strong','strong','weak','strong']
Play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
# encoder ==>convert string into neumerical form===>label encoder

# convert string to neumerical form
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
Outlook_encoder=le.fit_transform(Outlook)
print('Outlook_data',Outlook_encoder)
Temp_encoder=le.fit_transform(Temperature)
print('Temperature',Temp_encoder)
Humidity_encoder=le.fit_transform(Humidity)
print('Humidity',Humidity_encoder)
Wind_encoder=le.fit_transform(Wind)
print('Wind',Wind_encoder)

# zip
feature=list(zip(Outlook_encoder,Temp_encoder,Humidity_encoder,Wind_encoder))
print(feature)

# model creation
# naive bayes Model: 3 classification models

# 1.GAUSIAN Model : input_data-->contineous data
# 2.Multinomial : input_data-->descrete data(constant range data)
# 3.BERNOULLI : Similar to Multinomial model

# model creation
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(feature,Play)

print(model.predict([[2,0,0,0]]))