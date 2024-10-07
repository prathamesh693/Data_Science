# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:06:51 2024

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
row_label=['ro','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_label)
############################################
#slicing operation in DataFrame
#selecting row by index list
df2=df.iloc[[2,3,6]]
#select row by integer index
df2=df.iloc[1:5]
#select first row
df2=df.iloc[:1]
#select first three rows
df2=df.iloc[:3] #select first 3 rows
df2=df.iloc[-1:]   ###select last 1 rows
df2=df.iloc[-3:]   ###select last 3 rows
df2=df.iloc[::2]   ###select alternate rows

####select rows by index labels
df2= df.loc[['r2']]   #Select Row by label
df2
df2= df.loc[['r2','r3','r6']]   #Select rows by Index Label
df2=df.loc['r1':'r5']    #Select rows by Label Index 

df2= df.loc['r1':'r5':2] #Select Alternative rows with index
###########################################
#Using loc[] to take column slices
#loc[] syntax to slice column
#df.loc[:,start:stop:step]
## Select multiple colummn
df2= df.loc[:, ["Course","Fee","Duration"]]
#Select Random Columns
df2= df.loc[:, ["Course","Fee","Discount"]]
# Select columns between columns
df2= df.loc[:,'Fee','Discount']
## Select columns by range
df2 = df.loc[:,'Duration']
# Select columns by range
df2 = df.loc[:, 'Duration']
#Select column
#All the columns upto Duration
df2= df.loc[:,: 'Duration']
## Select every alternate column
df2 = df.loc[:,::2]
##############################################
##############################################
#Pandas.DataFrame.query() by examples
# Query all rows with Courses equals 'Spark'
df2= df.query("Course=='Spark'")
print(df2)
###################################
# not equals condition
df2= df.query("Course != 'Spark' ")
df2
#Pandas Add column to the DataFrame
#Add new column to the DataFrame
tutors =['Ram', 'sham', 'Ghansham', 'Ganesh', 'Ramesh','Mahesh','Sanket','Pratik']
df2= df.assign(TutorsAssigned=tutors)
print(df2)
#Add multiple columns to the DataFrame
MNCCompanies= ['TATA','HCL','Infosys','Google','Amazon','Microsoft','TCS','Accenture']
df2 = df.assign(MNCCompanies,tutors=tutors)
print(df2)
#Derive new column from Existing column
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent=lambda x: x.Fee * x.Discount / 100)
print(df2)
###############
#Append Column to Existing Pandas DataFrame
# Add New Column to the existing DataFrame
df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
print(df)
############################
#Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)
####################################
#Pandas Rename Column with Examples
import pandas as pd
import numpy as np
technologies={
              "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
              "Fee":[20000,25000,26000,27000,28000,np.nan,21000,22000],
              "Duration":["30 days","40 days","35 days","78 days","60 days","50 days","35 days","55 days"],
              "Discount":[1000,1020,1100,2300,1500,1800,2000,2700]
              }
df = pd.DataFrame(technologies)
df.columns
print(df.columns)
#Pandas Rename Column Name
# Replace existing DataFrame 
df.rename({'Courses':'Courses_List'})
# Interview question
# No. of data point and column and features of database