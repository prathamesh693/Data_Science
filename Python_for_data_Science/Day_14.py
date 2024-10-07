# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:21:38 2024

@author: ratho
"""
# interview most IMP dataframe

import pandas as pd
pd.__version__
#################################################
# Create using constructor
# create pandas DataFrame from list
# DataFrame comprise that is table or it create a table
import pandas as pd
technologies=[["Spark",20000,"30days",],["Pandas",20003,"40days"]]
df=pd.DataFrame(technologies)
print(df)
# this dataframe can create a two row and three column database
# the list are column and the containt of list are rows

# to give name's to the column's and row's
''' df=pd.DataFrame(data_list,columns=column_names,
    index=row_label)

here the columns can get the name's of the column and
the index can get the name's of the column 
#### their are an exception if we can pass the more column's 
but data are less then it will give us an error it also applicable
for row's
'''
column_names=['Course','fees','Duration']
row_label=['a','b']
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
###############################
df.dtypes
#########
# We can also assign custom data type to column
# set custom types to DataFrame
# standard method to create a DataFrame
import pandas as pd
technologies={
    "Course":["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    "Fee":[20000,25000,26000,27000,28000,21000,22000],
    "Duration":["30days","40days","35days","40days","65days","50days","55days"],
    "Discount":[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)
# Convert all types to best possible types
df2=df.convert_dtypes()
print(df2.dtypes)
# Change all column to same type
df=df.astype(str)
print(df.dtypes)
# Change types for One or Multiple columns
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)
# Convert Data type for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
# only chage particular columns data types
# if we want to change the datatype of some column and 
# other are remain same then we use it

df[cols]=df[cols].astype("float")
# as float
df.dtypes
###########################
#Ignore error
# if some time we can bymistaken change the datatype 
# that is not possible then we used errors="ignore"
# i.e. string to int

df=df.astype({"Course":int},errors='ignore')
df.dtypes
# it can't change the datatype but it ignore the errors

# it can show's the error or generate error
df=df.astype({"Course":int},errors='raise')
df.dtypes
##################################################
# convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df["Discount"]=pd.to_numeric(df["Discount"])
# to_numeric can convet into folat datatype not integer
df.dtypes
####################################################
import pandas as pd
technologies={
    "Course":["Spark","PySpark","Hadoop"],
    "Fee":[20000,25000,26000],
    "Duration":["30days","40days","35days"],
    "Discount":[11.8,23.7,13.4]
    }

df=pd.DataFrame(technologies)
df
############
# Convert DataFrame to CSV file
''' syntax
    DataFrame_name(.)to_csv(name_of_file.csv) 
'''
df.to_csv("data_file.csv")
###############################################
# To create DataFrame from CSV file

df=pd.read_csv('datafile.csv')
################################################
# Pandas DataFrame - Basic Operation
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
