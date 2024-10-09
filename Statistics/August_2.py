# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:22:50 2024

@author: ratho
"""
""" zero variance and near zero variance 
if there is no variance in the feature, then ML model
will not get any intelligence, so it is better to ignore
features
"""
import pandas as pd
df=pd.read_csv("C:/3-Statistics/ethinic_diversity.csv")
df.info()
df.Salaries.var() # to check the variance of a column
df.Salaries.var()==0
''' here emp_id and zip is nominal data
Salaries has 444195346.742  variance
'''
# None of them are equal to zero
df.Salaries.var(axis=0)==0
df.age.var(axis=0)==0
df.Zip.var(axis=0)==0

#########################################################################
import pandas as pd
import numpy as np

df=pd.read_csv("C:/3-Statistics/modified_ethnic.csv")
# check for all null values
df.isna().sum()
'''
Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries             0
age                 35
Race                25
dtype: int64
'''
''' 
create an imputer that creates nan values 
mean and median is used for numeric data mode is used
for discrete data(position,sex, MaritalDes)
'''
from sklearn.impute import SimpleImputer
mean_imputer =SimpleImputer(missing_values=np.nan, strategy='mean')
# create the dataframe for imputer
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))
#check the dataframe
df['Salaries'].isna().sum()
# 0
median_imputer =SimpleImputer(missing_values=np.nan, strategy='median')
# create the dataframe for imputer
df['age']=pd.DataFrame(median_imputer.fit_transform(df[["age"]]))
df['age'].isna().sum()
# 0
mode_imputer =SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# create the dataframe for imputer
df['Sex']=pd.DataFrame(mode_imputer.fit_transform(df[["Sex"]]))
df['age'].isna().sum()
# 0
df['MaritalDesc']=pd.DataFrame(mode_imputer.fit_transform(df[["MaritalDesc"]]))
df['MaritalDesc'].isna().sum()
# 0
################################################################################
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

X,y=make_classification(n_samples=1000, n_features=20, n_informative= 2,n_redundant=10,n_clusters_per_class=1,weights=[0.99],flip_y=0,random_state=1)
''' Parameters
n_samples : the total no. of samples to generate
here 1000 samples will be created
n_features: the total no. of features (column) in the database
each have 20 features
n_informative: the no. of informative features
n_redundant :
    the no. of redundant features .
    these features are generated as random linear combinations of the dataset
n_clusters_per_class:
    each class have one cluster of ponits
weinght:
    the properties of same class is assing to the database
flip:
    

'''
# show the original class distribution
print("Original class distribution:", np.bincount(y))
# step2: apply SMOTE to balanced the dataset
smote=SMOTE(random_state=42)
X_res,y_res=smote.fit_resample(X, y)
# show the resampled class distribution
print("Resampled class distribution:",np.bincount(y_res))














