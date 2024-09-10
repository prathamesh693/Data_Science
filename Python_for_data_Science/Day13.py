import pandas as pd
import numpy as np

george= pd.Series([10,7,1,22],
    index=["1968","1969","1970","1970"],
    name="george_Songs")
george['1968']

# updating in series
''' updating value in a series can be a little tricky as will.
to update a value for a given index label,
the standard index assignment operation works'''

george['1969']=68
george['1969']
george
# Deletion 
# the del statemetn appears to have problems with duplicate index
s=pd.Series([2,3,4], index=[1,2,3])
del s[1] # it can delete the value as well as index i.e.
s
##################################################
# convert Types
''' String use.astype(str) numeric use pd.to_numeric
integer use astype(int),
note that this will fail with NaN
datetime use pd.to_datetime
'''
songs_66=pd.Series([3.0,None,11.0,9.0],
        index=["Geroge","Ringo","john","Paul"], name="counts")
songs_66.dtype # the dtype is an properties not method 
# the word dtype give us the data type of a series of pd
# The output is ('float64')

# pd.to_numeric(songs_66.apply(str))

# it can try to change the data type but there will be error
# because None value are not acceptable in series

pd.to_numeric(songs_66.astype(str),errors='coerce')
# if we pass  errors="coerce",
# we can see that it supports many formates

# fillna(-1) dealing with None
# This method replace None into with a given values
songs_66=songs_66.fillna(-1)
songs_66
songs_66=songs_66.apply(int) # it can change the data type as int
songs_66.dtype
# output will be ('int64')
songs_66
songs_66=songs_66.apply(str) # it can change the data type as string 
songs_66.dtype
# it can give ('0') because some time code not consider pointing value
##################################################
# droping None value using the dropna() function
# it can drop the None value as well as information of that None value
# also delete all the data in the None rows
songs_66=pd.Series([3.0,None,11.0,9.0],
        index=["Geroge","Ringo","john","Paul"], name="Counts")
songs_66=songs_66.dropna()
songs_66
##################################################
# append, combining, and joining two series
songs_69=pd.Series([7,16,21,39],
        index=['Ram','sham','Krishna','BalRam'],
        name='counts')
# to concatinate two series 
song=songs_66._append(songs_69)# this is the old method not work in new version
# to concatinate two series in a data 
pd.concat([songs_66,songs_69])
################################################
# Ploting the Series in python using matplotlib
import matplotlib.pyplot as plt
# pyplot in module inside the module that why 
# we need to write (.) to access it
songs_66=pd.Series([3.0,4.6,11.0,9.0],
        index=["Geroge","Ringo","john","Paul"], name="Counts")

songs_69=pd.Series([7,16,21,39],
        index=['Ram','sham','Krishna','BalRam'],
        name='counts')

fig = plt.figure()
songs_69.plot()
plt.legend()
#########################################
# if we give an None value to the series it can't overwrite 
# it can only give one or one column of one series or not 
# giving any column of one series
fig =plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()
##########################################
# To plot histogram in python
import numpy as np
data=pd.Series(np.random.rand(500),name='500_random')
fig =plt.figure()
ax = fig.add_subplot(111)
data.hist()
########################################################################