# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:15:32 2024

@author: ratho
"""
# Shuffle DataFrame is more important
# pandas shuffle dataframe rows
import numpy as np
import pandas as pd
technologies={
              "Course":["Spark","PySpark","Hadoop","Python","pandas",None,"Spark","Python"],
              "Fee":[20000,25000,26000,27000,28000,np.nan,21000,22000],
              "Duration":["30 days","40 days","35 days","78 days","60 days","50 days","35 days","55 days"],
              "Discount":[1000,1020,1100,2300,1500,1800,2000,2700]
              }
df = pd.DataFrame(technologies)
print(df)
# pandas shuffle dataframe rows
# shuffle the dataframe rows and return all rows
df1=df.sample(frac=0.5) # 50% shuffle the dataframe rows
                        # and give 50% output
df2=df.sample(frac=1) # 100% shuffle the dataframe
print(df1)
print(df2)
##################
# create a new index starting from zero
df2=df.sample(frac=1).reset_index()
print(df2)
# Drop the old index and only show the new index
df2=df.sample(frac=1).reset_index(drop=True)
print(df2)
############################
# joining of dataframe is important for data scientist
'''
1.inner join # mostly used
2.left join 
3.right join
4.outer join 
'''
""" inner join only join the common row in both the 
table. """
 
technologies1={
              "Course":["Spark","PySpark","pandas","Python"],
              "Fee":[20000,25000,26000,27000],
              "Duration":["30 days","40 days","35 days","60 days"],
              "Discount":[1000,1020,1100,2300]
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_labels)

technologies2={"Course":["Spark","java","python","go"],
               "Discount":[1000,1020,1100,1520]
               }
index_labels2=['r1','r6','r3','r7']
# index_labels2=['r1','r5','r4','r6']
df2=pd.DataFrame(technologies2,index=index_labels2)
# pandas  join
df3=df1.join(df2, lsuffix="_left",rsuffix="_right")
print(df3)
''' in this join df2 is join into the left side of df1
and store to df3 the joining is based on the index of
both the table.
If the index are the same then both column are join and
if the column are not same but index are same then it will
shows as non.
'''
# inner joining of DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how="inner")
print(df3)
# left joining of DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how="left")
print(df3)
# right joining of DataFrame
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how="right")
print(df3)
###########################
''' merging the table without showing the repeated column
it can shown by once.
'''
technologies1={
              "Course":["Spark","PySpark","pandas","Python"],
              "Fee":[20000,25000,26000,27000],
              "Duration":["30 days","40 days","35 days","60 days"],
              "Discount":[1000,1020,1100,2300]
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_labels)

technologies2={"Course":["Spark","java","python","go"],
               "Discount":[1000,1020,1100,1520]
               }
index_labels2=['r1','r5','r4','r6']
df2=pd.DataFrame(technologies2,index=index_labels2)

# using pandas.merge()
df3=pd.merge(df1, df2)
# using DataFrame.merge()
df3=df1.merge(df2)
### Both give same output
''' concat() function can add both the table in vertical
the values of both the table are merge even the rows are 
common or not it will concate both the table.
'''
import pandas as pd
df=pd.DataFrame({"Course":["Spark","PySpark","Python","pandas"],
                 "Fee":[20000,25000,24000,24000]})
df1=pd.DataFrame({"Course":["pandas","Hadoop","Hyperion","java"],
                 "Fee":[25000,25200,24500,24900]})
# using pandas.concat() to concat two DataFrame
data=[df,df1]
df2=pd.concat(data)
print(df2)
###########################
# multiple DataFrame
df=pd.DataFrame({"Course":["Spark","PySpark","Python","Pandas"],
                 "Fee":['20000','25000','22000','24000']})
df1=pd.DataFrame({"Course":["Unix","Hadoop","Hyperion","java"],
                 "Fee":['25000','25200','24500','24900']})
df2=pd.DataFrame({"Duration":["30day","40day","35day","60day"],
                 "Discount":[20000,25000,24000,24000]})
# Appending multiple DataFrame
df3=pd.concat([df,df1,df2]) # Here index are repeated
# df3=pd.concat([df,df1,df2]).reset_index(drop=True)
# the second statement give an index properly
print(df3)











