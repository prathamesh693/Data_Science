# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:15:49 2024

@author: ratho
"""
import pandas as pd
import numpy as np
technologies={
              "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
              "Fee":[20000,25000,26000,27000,28000,np.nan,21000,22000],
              "Duration":["30 days","40 days","35 days","78 days","60 days","50 days","35 days","55 days"],
              "Discount":[1000,1020,1100,2300,1500,1800,2000,2700]
              }
df = pd.DataFrame(technologies)
######################
# quick examples of get the no. of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count
##############################
df = pd.DataFrame(technologies)
rows_count=df.shape[0] # return only no.of rows i.e(0)
rows_count
col_count=df.shape[1] # return only no.of column i.e(1)
print(rows_count)
print(col_count)

both=df.shape
both
# it will give both the no. of column and row
########################
import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3

df2=df.apply(add_3) 
# apply function is use to
# apply any function to the dataframe
df2
# This can change the value's of all dataframe
#######
# apply function on a single/specific column
df2=((df.A).apply(add_3))
print(df2)
# Using apply function single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]
# apply to multiple columns
df[["A","B"]]=df[["A","B"]].apply(add_4)
df
# apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2
#################################
# apply() function on selected list of multiple columns
df=pd.DataFrame(data)
df[["A","B"]]=df[["A","B"]].apply(add_3)
print(df)
##############
#using pandas.DataFrame.transform() to apply function on column
# using DataFrame.transform()
def add_2(x):
    return x+2
df=df.transform(add_2)
print(df)
#############
# using pandas.DataFrame.map() to single column
df["A"]=df["A"].map(lambda A: A/2.0)
print(df)
#############
# using Numpy function on single column
# using DataFrame.apply() & [] operator
import numpy as np
df["A"]=df["A"].apply(np.square)
# square the value of column A
'''
if we have to use function inside function then not
use round bracess for second function
'''
print(df)
############
# another method to apply square on column
# using Numpy.square() method
# using numpy.square() and [] operator
df["A"]=np.square(df["A"])
print(df)
############
technologies={
              "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
              "Fee":[20000,25000,26000,27000,28000,np.nan,21000,22000],
              "Duration":["30 days","40 days","35 days","78 days","60 days","50 days","35 days","55 days"],
              "Discount":[1000,1020,1100,2300,1500,1800,2000,2700]
              }
df = pd.DataFrame(technologies)
print(df)

# use groupby() to compute the sum
''' this function can sum all the similar intity of 
a column and the sum of their values
'''
df2=df.groupby(['Course']).sum()
# it can only sum the value it is not applicable for string
# (it concatinate the string) and also remove the none column
print(df2)
###############
# group of multiple column
df2=df.groupby(['Course','Duration']).sum()
print(df2)
###########
# add Index to the grouped data
# add row index to the group by result
df2=df.groupby(['Course','Duration']).sum().reset_index()
print(df2)
####################################################################
import numpy as np
import pandas as pd
technologies={
              "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
              "Fee":[20000,25000,26000,27000,28000,np.nan,21000,22000],
              "Duration":["30 days","40 days","35 days","78 days","60 days","50 days","35 days","55 days"],
              "Discount":[1000,1020,1100,2300,1500,1800,2000,2700]
              }
df = pd.DataFrame(technologies)
df.columns
## popular is df.columns
# get the list of all column names from headers
column_headers=list(df.columns.values)
print("The column Header: ",column_headers)
#############
#using list(df) to get the column headers as a list 
column_headers=list(df.columns)
print(column_headers)


















