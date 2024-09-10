
''' data type, operation, list, lict, tupple, function, lambda,
generator, decorator.
OOP: inheritance, coparator, 
'''
################################################################
##################### Python for Data Science (pandas,matplotlib, ) #################
##################### in JD ####################
''' pandas
1. series
2. columns
'''
##############################################################
# series in pandas
''' a series is used to model one dimensional data,
similar to a list in python.
the series object also has a few more bits
of data including an # index and a name
'''
# synatax of series
import pandas as pd
songs2 = pd.Series([143,145,38,13],name="counts")
# it is easy to inspect the index of a series
songs2.index
# the index can be string based as well,
# in which case pandas indicates
# that the datatype for the index is object(not string)

songs3 = pd.Series([145,142,38,13],name="counts",
   index=["Paul", "John", "George", "ringo"])
songs3.index
songs3
# the NaN value
# this value stands for Not a Number,
# and is 
# operations. (similar to NULLL in SQL).
# if you load data from a CSV file,
# an empty value for an otherwise

# numeric column will become NaN.
import pandas as pd
f1=pd.read_csv("P:/Data_Science/Python_for_data_Science/age.csv")
f1

df=pd.read_excel("P:/Data_Science/Python_for_data_Science/Bahaman.xlsx")
# none, NaN, nan, and Null are synonyms
# the series object behaves similarly to a NumPy array.
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
# 142
numpy_ser[1]
# They both have methods in common
songs3.mean()
numpy_ser.mean()
############################################33
# THE PANDAS SERIES DATA STRUCTURE PROVIDES
# SUPPORT FOR THE BASIC CRUD
# operations-create, read, update, and delete.
# creation of series

george= pd.Series([10,7,1,22],
    index=["1968","1969","1970","1970"],
    name="george_Songs")
print(george)
''' The previous example illustrates an 
interesting feature of pandas-the index
values are strings and they are not unique. This can cause some
confusion, but can also be useful when duplicate index items
are needed.'''
###############################################################
# Reading
# To read or select the data from a series
george= pd.Series([10,7,1,22],
    index=["1968","1969","1970","1970"],
    name="george_Songs")
george['1968']

george['1970']
# we can iterate over data in a series
# as well. when iterating over a series
for item in george:
    # we can access or read all the data in series
    print(item)
# 10 7 1 22
###################################################