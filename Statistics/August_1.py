# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:53:09 2024

@author: ratho
"""
import pandas as pd
import seaborn as sns

df=pd.read_csv("C:/3-Statistics/ethinic_diversity.csv")
df.head()
sns.boxplot(df.Salaries)
# to plot the box of column Salaries
sns.boxplot(df.age)
# let us calculate IQR
IQR = df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
IQR

lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
lower_limit
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR
upper_limit

# Trimming
import numpy as np
outlies_df= np.where(df.Salaries>upper_limit,True,
                     np.where(df.Salaries<lower_limit,True,False))
# you can check outlier_df column in variable explorer
df_trimmed=df.loc[~outlies_df]
df.shape
# (310,13)
df_trimmed.shape
# (306,13) it can trimmed the outlier rows 
sns.boxplot(df_trimmed.Salaries)
# Replacement Technique
# Drawback of trimming technique is we are losing the data
df=pd.read_csv("C:/3-Statistics/ethinic_diversity.csv")
df.describe()
# map all the outlier values ot upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
sns.boxplot(df_replaced[0])
""" if the values are greater than upper_limit map it to upper limit , 
and less than lower_limit map it to lower limit, 
if it is within the range then keep as it is """

# Winsorizer
# removing outlier using winsorizer
# best outlier remover i.e. best time and space complexity
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',
                  tail='both',fold=1.5,
                  variables=['Salaries'])

df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df["Salaries"])
sns.boxplot(df_t["Salaries"])

