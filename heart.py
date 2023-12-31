# -*- coding: utf-8 -*-
"""heart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NzPXRYvGcc0EvEzLGpnpzP9273fEnyrB

Import The Libreries
"""

import pandas as pd

"""import the data set"""

data=pd.read_csv("/content/heart.csv")

"""Taking care of missing value"""

data.isnull().sum()

"""find duplicat value"""

data_dup=data.duplicated().any()
data_dup

data=data.drop_duplicates()
data_dup=data.duplicated().any()
data_dup

"""Data processing"""

cate_val=[]
cont_val=[]
for column in data.columns:
  if data[column].nunique()<=10:
    cate_val.append(column)
  else:
    cont_val.append(column)

cate_val

cont_val

"""Encoding categorical Data"""

cate_val

data['cp'].unique()

cate_val.remove('sex')
cate_val.remove('target')
data=pd.get_dummies(data,columns=cate_val,drop_first=True)

data.head()

"""Feature scling"""

from sklearn.preprocessing import StandardScaler

st=StandardScaler()
data[cont_val]=st.fit_transform(data[cont_val])

data.head()

"""Splitting the Dataset into Train and test set"""

x=data.drop('target',axis=1)
y=data['target']
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

x_train

x_test

"""Logistic Regression"""

data.head()

from sklearn.linear_model import LogisticRegression

log = LogisticRegression()
log.fit(x_train,y_train)

y_pred1=log.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred1)

from sklearn import metrics

confusion_matrix1 = metrics.confusion_matrix(y_test,y_pred1)
confusion_matrix1

"""SVC

"""

from sklearn import svm

svm=svm.SVC()
svm.fit(x_train,y_train)

y_pred2=svm.predict(x_test)
accuracy_score(y_test,y_pred2)

confusion_matrix2 = metrics.confusion_matrix(y_test,y_pred2)
confusion_matrix2

"""KNeighbores"""

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier()

knn.fit(x_train,y_train)

y_pred3 = knn.predict(x_test)

accuracy_score(y_test,y_pred3)

confusion_matrix3 = metrics.confusion_matrix(y_test,y_pred3)
confusion_matrix3

score=[]
for k in range(1,40):
  knn=KNeighborsClassifier(n_neighbors=k)
  knn.fit(x_train,y_train)
  y_pred=knn.predict(x_test)
  score.append(accuracy_score(y_test,y_pred))

score

knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
accuracy_score(y_test,y_pred)

confusion_matrix = metrics.confusion_matrix(y_test,y_pred)
confusion_matrix

"""Non-Linear Machinlearning algo"""

data=pd.read_csv("/content/heart.csv")

data.head()

data=data.drop_duplicates()

x=data.drop('target',axis=1)
y=data['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

"""Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)

y_pred4=dt.predict(x_test)
accuracy_score(y_test,y_pred4)

confusion_matrix4 = metrics.confusion_matrix(y_test,y_pred4)
confusion_matrix4

"""Random Forest Clssifier"""

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier()
rf.fit(x_train,y_train)

y_pred5=rf.predict(x_test)

accuracy_score(y_test,y_pred5)

confusion_matrix5 = metrics.confusion_matrix(y_test,y_pred5)
confusion_matrix5

final_data=pd.DataFrame({'Models':['LR','SVC','KNN','DT','RF'],
'ACC':[accuracy_score(y_test,y_pred1),
       accuracy_score(y_test,y_pred2),
       accuracy_score(y_test,y_pred3),
       accuracy_score(y_test,y_pred4),
       accuracy_score(y_test,y_pred5)]})

final_data

import seaborn as sns

sns.barplot(x=final_data['Models'],y=final_data['ACC'])

x=data.drop('target',axis=1)
y=data['target']

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(x,y)

"""Prediction New Data"""

import pandas as pd

new_data=pd.DataFrame({
    'age':52,
    'sex':1,
    'cp':0,
    'trestbps':125,
    'chol':212,
    'fbs':0,
    'restecg':1,
    'thalach':168,
    'exang':1.0,
    'oldpeak':2,
    'slope':2,
    'ca':2,
    'thal':3,
    },index=[0])

new_data

p=rf.predict(new_data)
if p[0]==0:
  print('No disease')
else:
  print('Having Disease')

