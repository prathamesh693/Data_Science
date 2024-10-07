# -*- coding: utf-8 -*-
"""
Created on Thu Apr  10 08:19:44 2024

@author: ratho
"""
####################

import pandas as pd
import numpy as np
technologies={
    "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
    "Fee":[20000,25000,26000,27000,np.nan,28000,21000,22000],
    "Duration":["30days","40days","35days","40days","65days","50days","35days","55days"],
    "Discount":[1000,1020,1500,2300,1000,2500,1200,1300]
    }
row_label=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_label)
'''
#drop column by name
#drop for column
'''
d21=df.drop(df.index[2:])
'''
#drop column by index
'''
print(df.drop(df.columns[1],axis=1))
'''
######################################
'''
df=pd.DataFrame(technologies)
#using inplace=true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)
'''
################################
'''
df=pd.DataFrame(technologies)
#drop two or more columns by  label name
df2=df.drop(['courses','fee'],axis=1)
print(df2)
'''
##########################################
#drop two or more columns by index
'''
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)   #imp: se list inside list for column by index
print(df2)
'''
#######################################################
#drop columns from the list of columns
'''
df=pd.DataFrame(technologies)
df.columns
liscol=['courses','fee']
df2=df.drop(liscol,axis=1)
print(df2)
'''
#####################################################
#remove columns from the data inplace
'''
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df
'''
#########################################
#Interview Question
#iloc: accessing column using index
#loc: accessing column using names
#pandas select rows by index (position/label)
'''
import pandas as pd
import numpy as np
technologies={
    'courses':['spark','pyspark','hadoop','python','pandas',None,'java'],
    'fee':[20000,25000,26000,22000,24000,np.nan,22000],
    'duration':['30day','40day','','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
row_labels=['r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
'''
#df.iloc[startrow:endrow,startcolumn:endcolumn]
'''
df=pd.DataFrame(technologies,index=row_labels)
'''
#below is a quick example
'''
df2=df.iloc[:,0:2]
df2
'''
#this line uses a slicing operator to get Dataframe
#Item by index
#The first slice [:] indicates to return all rows
#the second slice specifies that only columns
#between 0 and 2 (excluding 2) should be returned
'''
df2=df.iloc[0:2,:]
df2
'''
#in this case, the first slice [0:2] is requesting only row 0
#through of the data frame. 
#the second slice [:] indicates that all columns are required
#########################################################
# Slicing specific rows and Columns using the iloc attribute
'''
df3=df.iloc[1:2,1:3]
df3
'''
#select rows by integer index
'''
df2=df.iloc[2]
df2
'''
######################################################
'''
df2=df.iloc[[2,3,6]] #select rows by index list
df2=df.iloc[1:5] #select rows by integer index Raange
df2=df.iloc[:1] #select first row
df2=df.iloc[-1:] #select last row