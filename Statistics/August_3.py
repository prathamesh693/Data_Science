# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:22:45 2024

@author: ratho
"""
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
X,y=make_classification(n_samples=1000, n_features=20, n_informative= 2,n_redundant=10,n_clusters_per_class=1,weights=[0.99],flip_y=0,random_state=1)
# show the original class distribution
print("Original class distribution:", np.bincount(y))
# step2: apply SMOTE to balanced the dataset
smote=SMOTE(random_state=42)
X_res,y_res=smote.fit_resample(X, y)
# show the resampled class distribution
print("Resampled class distribution:",np.bincount(y_res))
# origial class distribution
print(f'Original class distribution: {np.bincount(y)}')
from sklearn.model_selection import train_test_split
# step2: split the data into training and testing sets
X_train, X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=42)

#step3:apply SMOTE to balance the training dataset
smote=SMOTE(random_state=42)
X_train_res,y_train_res=smote.fit_resample(X_train,y_train)

# show the new class distribution after applying SMOTE
print(f'Resampled class distribution: {np.bincount(y_train_res)}')

#Step4: Train a classifier on the balanced dataset
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(random_state=42)
clf.fit(X_train_res,y_train_res)

# step5: Evaluate the classifier on the test set
y_pred = clf.predict(X_test)
from sklearn.feature_selection import confusion_matrix # wrong
print("Comfusion Matrix:")
print(confusion_matrix(y_test,y_pred))
#######################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# generate a sample dataset 
np.random.seed(0)
data=np.random.exponential(scale=2.0,size=1000)
df=pd.DataFrame(data,columns=["Value"])

# perform log transformation
df['LogValue']=np.log(df["Value"])

# plot the original and log-transformed data
fig,axes=plt.subplots(1,2,figsize=(12,6))

# Original data
axes[0].hist(df["Value"],bins=30,color='blue',alpha=0.7)
axes[0].set_title("Original Data")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

# log transformed data
axes[1].hist(df["LogValue"],bins=30,color='green',alpha=0.7)
axes[1].set_title("Log-transformed Data")
axes[1].set_xlabel("Log(Value)")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show

