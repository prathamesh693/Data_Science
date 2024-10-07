# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:13:34 2024

@author: ratho
"""
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
print(df)
#######################################
# DataFrame properties 
df.shape
#(8,4)
df.size
#32
df.columns 
df.columns.values
df.index
df.dtypes
df.info
''' important properties are 
shape
size 
columns
dtypes
'''
###########################################
''' Machine Learning Process Steps

1. Understanding objective
2. data dictionary
3. EDA - exploration or to understand 
4. Data Processing 
5. Model 
6. Evaluation 
7. Deploy
8. Monitoring and  Maintenance
'''
# Accessing Column content in two way 
'''
1. by column name and 
2. by index
'''
# 1. by column name
df['Fee']
# accessing two column 
cols=['Fee','Duration']
df[cols]
# or 
df[['Fee','Duration']]

#2. by index


####################3
# select certain rows and assign it to another dataframe
df2=df[6:] # want all rows starting from 6 to end 
df2=df[:5] # to access first 4 rows
df2
#Accessing rows and column 
''' Syntax
df2=df[rows column]
'''

df2=df [:2 :2]
df2
############
# Accessing certain cell from the dataframe
df['Duration'][3]
###############
# Substacting specific value from a column
df['Fee']=df['Fee']-500 # reduce all the fees by 500
df['Fee']
##############
''' mean 
    median
    std.deviation
'''
#pandas to manipulate dataframe
# describe dataframe
# describe dataframe for all numeric column
df.describe()
''' it gives output

                    Fee     Discount
    count      7.000000     8.000000
    mean   23642.857143  1477.500000
    std     3132.015934   597.177887
    min    19500.000000  1000.000000
    25%    21000.000000  1015.000000
    50%    24500.000000  1250.000000
    75%    26000.000000  1700.000000
    max    27500.000000  2500.000000
'''
########################################
# rename() -Renames pandas DataFrame columns
df=pd.DataFrame(technologies, index=row_label)

# Assign new header by setting new column names.
df.columns=['a','b','c','d']
df
########################
# Rename column names using rename() method
df=pd.DataFrame(technologies, index=row_label)
df.columns=['a','b','c','d']
# for row axis = 0 and for column axis = 1
# it can change a and b column and other are remain same
df2=df.rename({'a':'c1','b':'c2'}, axis=1) 
# it can change c and d column and other are same as a and b not 
# above changed name
df2=df.rename({'c':'c3','d':'c4'}, axis='columns')
# same concept here also
df2=df.rename(columns={'a':'c1','b':'c2'})
####################
# Drop DataFrame rows and columns 
df=pd.DataFrame(technologies,index=row_label)

# Drop rows by labels
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
# to drop a particular rows i.e. row 1 and row 3
df1
# delete rows by index range
df1=df.drop(df.index[2:])
df1
# When you have default indexes for rows
df=pd.DataFrame(technologies)
df1= df.drop(0)
df1
##########
# multiple rows drop
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0) # it will delete row 0 and row 3
df1
df1=df.drop(range(0,2)) # it will delete 0 and 1
df1
