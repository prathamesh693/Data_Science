# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:21:04 2024

@author: ratho
"""
import numpy as np
import pandas as pd
df=pd.DataFrame({"Course":["Spark","PySpark","Python","Pandas"],
                 "Fee":['20000','25000','22000','24000']})
## convert rows into the list formate 
# using the Course.values and tolist()
col_list=df.Course.values # it is the array data type
print(col_list)
print(type(col_list))
col_list=df.Course.values.tolist() #it is list data type
print(col_list)
print(type(col_list))
# using Series.values.tolist()
# another method/ techniques
col_list=df["Course"].values.tolist()
print(col_list)
# Using list() function
col_list=list(df["Course"])
print(col_list)
# convert to numpy array
col_list=df["Course"].to_numpy()
######################################
#############Numpy#####################
''' while a python list can contain different 
data types within a single list,
all of the element in a numpy array 
should be homogeneous.
'''
# array in Numpy
# numpy is use in linear algebra
# like a dimensionality, expanding and murging of matrix
'''
#interview important

x=3 ---scalar
x=[10,20]---vector (single dimensional array)
x=[[10,20],[30,40]] ---matrix (two dimensional array)
x=[[[]]] ----tensor(multi dimensional array)
'''
#create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)
# output is:
    # [10,20,30]

# multi-dimension array
arr_mul=np.array([[2,5,8,9],[45,54,85,89],[15,16,12,19]])
print(arr_mul)
''' Output is :
    [[ 2  5  8  9]
     [45 54 85 89]
     [15 16 12 19]] '''
# to convert a list into three dimensional array
# so use this 
# the ndmin param to specify how many minimum
# dimension you wanted to create an arraywith minimum
# dimension
arr=np.array([[1,2,3,5,8],[5,9,6,5]], ndmin=3)
print(arr)
'''ValueError: setting an array element with a sequence. 
The requested array has an inhomogeneous shape after 
1 dimensions. The detected shape was (2,)
 + inhomogeneous part.'''
###
arr=np.array([1,2,3,5,8], ndmin=3)
print(arr) # it give an three dimension array
###
# change the data type using dtype parameter
arr=np.array([1,2,3,5,8], dtype=complex)
arr
# get the dimension of array
arr =np.array([[1,2,5,3],[5,9,12,35],[21,23,12,18]])
print(arr.ndim)
print(arr)

arr=np.array([10,20,30])
print("Each item is of the type ",arr.dtype)

arr =np.array([[1,2,5,3],[5,9,12,35],[21,23,12,18]])
print("Array size:", arr.size)
print("shape:", arr.shape)
# in shape 3 rows and 4 column
###########
# creating array from the list with data type float
arr =np.array([[1,2,5,3],[5,9,12,35]], dtype=float)
print("array created by using list: \n", arr)
###############
# create a sequence of integers using arange()
# create a sequence of integers 
# from 0 to 31 with steps of 3
arr=np.arange(0,31,3) # it like a table of 3
print("A sequential array with steps of 3:\n",arr)
########
arr=np.arange(11)
print(arr)# it will give an 0 to 10 range values
print(arr[2])# access single element using index
print(arr[-2]) # access single element using index(-ve)

# multi dimension array indexing 
# to access using array indexing
arr=np.array([[1,2,5,3],[5,9,12,35],[21,23,12,18]])
print(arr)
''' output:
[[ 1  2  5  3]
 [ 5  9 12 35]
 [21 23 12 18]]
'''
print(arr.shape)
# (3,4)
print(arr[1,2])
# second row and third column (index starting form 0)
# 12
print(arr[1,-2])
# 12 # 2st row and last second element 

# Access array using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2] # start:end:in step of 2
print(x) # output: 2 4 6 8
#############
x=arr[-1:2:-1]
print(x)
x=arr[-2:10]
print(x)
####
# multi-dimensional array slicing 
arr_mult =np.array([[1,2,5,3],[5,9,12,35],[21,23,12,18]])

arr_mult[1,2]

arr_mult[1,:] # second row and all element
#Output: array([ 5,  9, 12, 35])
arr_mult[:,1]# second column of all rows element
#Output: array([ 2,  9, 23])
x=arr_mult[:3, ::2]
print(x)
''' Output:
    [[ 1  5]
   [ 5 12]
   [21 12]]'''
# accessing one to 3rd coloumn in step of 2 of all rows

''' our multi-dimensional array is :
    
    array([[ 1,  2,  5,  3],
           [ 5,  9, 12, 35],
           [21, 23, 12, 18]])
'''
####################################################