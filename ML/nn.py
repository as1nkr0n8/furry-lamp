# -*- coding: utf-8 -*-
"""NN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19TGIaFZY1x3qabN-6fBMrDYv2en0FtP5
"""

'''import sklearn
import numpy as np
from sklearn.neural_network import MLPClassifier

import pandas
df = pandas.read_csv('dataset with intensity 3-5-new.csv')
#print()
#Input array
X=np.array(df[['Avg.PCC','Avg.Motion..','Average Intensity','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

#Output
y=np.squeeze(np.array(df[['Compression.Preset']]))
#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
print(X)
print(y.shape)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10,5,5,5,6), random_state=1)

clf.fit(X, y)

y_pred = clf.predict(X)
print(X)
print(y)
print(y_pred)

error = np.mean(np.equal(y,y_pred))
print(error)'''


import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

import pandas
df = pandas.read_csv('dataset with intensity 3-5-new.csv')
#print()
#Input array
X=np.array(df[['Avg.PCC','Avg.Motion..','Average Intensity','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

#Output
y=np.squeeze(np.array(df[['Compression.Preset']]))
#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
print(X)
print(y.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


#clf = RandomForestClassifier(n_estimators=100, max_depth = 7, random_state=0)
clf = GradientBoostingClassifier(n_estimators=40, max_depth = 2, random_state=0)

clf.fit(X_train, y_train)

y_pred_t = clf.predict(X_train)

train_error = np.mean(np.equal(y_train,y_pred_t))
print(train_error)


y_pred = clf.predict(X_test)
print(y_pred)

test_error = np.mean(np.equal(y_test,y_pred))
print(test_error)