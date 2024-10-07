# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:14:49 2024

@author: ratho
"""
import numpy as np
arr_mult =np.array([[1,2,5,3],[5,9,12,35],[21,23,12,18]])
# integer array indexing
arr=np.arange(35).reshape(5,7)
print(arr)
###########
# Boolean array indexing
''' this method is use to ...
if we want some rows and some are not wanted then
will use it.
&&& Syntax &&&   0th   1st  2nd
rows=np.array([False,True,True])

:: not give an 0th rows olny give an 1st and 2nd rows
'''
arr=np.arange(12).reshape(3,4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
rows=np.array([True,False,True])
print(rows) # it give only 0th and 2nd rows
wanted_rows=arr[rows, :] # assing the rows without can't print
print(wanted_rows)
####################
#use asarray()
list=[20,30,40] # this is a list
array=np.asarray(list) # converting list into array
print("Array:",array)
print(type(array))

# Numpy Array Properties:
    
    #ndarray.shape
    #ndarray.ndim
    #ndarray.itemsize
    #ndarray.size
    #ndarray.dtype

# ndarray.shape
# shape properties of ndarray
# to get the shape of a python numpy array use shape properties

# shape
array=np.array([[1,2,3,],[4,5,6]])
array
print(array.shape) # (2,3)

# resize the array
array.shape=(3,2)
# or both are same
new_array=array.reshape(3,2)
print(new_array)
print(new_array.shape)
#####################
# arithmatic Operation on Array
arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])
arr1
# add()
add_arr=np.add(arr1,arr2)
print(f"Addition two arrays:\n{add_arr}")
# Adding two arrays
'''
[[ 0,  1,  2,  3], + [1,2,3,4] = [[ 1  3  5  7]
 [ 4,  5,  6,  7],               [ 5  7  9 11]
 [ 8,  9, 10, 11],               [ 9 11 13 15]
 [12, 13, 14, 15]]               [13 15 17 19]]
'''
# substraction 
sub_arr=np.subtract(arr1,arr2)
print(f"Substraction of two arrays:\n{sub_arr}")
# explaination
'''
[[ 0,  1,  2,  3], - [1,2,3,4] = [[-1 -1 -1 -1]
 [ 4,  5,  6,  7],               [ 3  3  3  3]
 [ 8,  9, 10, 11],               [ 7  7  7  7]
 [12, 13, 14, 15]]               [11 11 11 11]]
'''
# multiplication
mul_arr=np.multiply(arr1,arr2)
print(f"Multiplication of two arrays:\n{mul_arr}")
#Explaination
'''
[[ 0,  1,  2,  3], * [1,2,3,4] = [[ 0  2  6 12]
 [ 4,  5,  6,  7],               [ 4 10 18 28]
 [ 8,  9, 10, 11],               [ 8 18 30 44]
 [12, 13, 14, 15]]               [12 26 42 60]]
'''
# division
div_arr=np.divide(arr1,arr2)
print(f"division of two arrays:\n{div_arr}")
''' Output 
[[ 0.          0.5         0.66666667  0.75      ]
 [ 4.          2.5         2.          1.75      ]
 [ 8.          4.5         3.33333333  2.75      ]
 [12.          6.5         4.66666667  3.75      ]]
'''
# To perform reciprocal operation
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"After applying reciprocal to array:\n{rep_arr1}")

# Numpy.power()/ power operation
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f'after applying power function to array:\n{pow_arr1}')

# power of one array to other array
arr1=np.array([3,10,5])
print("My 1st array is:\n",arr1)
arr2=np.array([3,2,4])
print("My 2nd array is:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(pow_arr2)
# 2nd array is the power of 1st array
#Output:[ 27 100 625]

arr1=np.array([7,20,13])
print("My 1st array is:\n",arr1)
arr2=np.array([3,5,2])
print("My 2nd array is:\n",arr2)
# mod()
mod_arr=np.mod(arr1,arr2)
print(mod_arr)
##################
# creating an empty array
# use in image processing it help to reduce the size of image
from numpy import empty
a=empty([3,3])
print(a) # it is empty but it give an garbage value
# don't worry about it

# Create a zeros 
from numpy import zeros
a = zeros([3,5])
print(a) # it will give an zeros array (arrays values)

#Create a one values array
# use of one and zeros array in igen values
from numpy import ones as on
a=on([2,2])
print(a)
######################
# creating array with vstack
from numpy import array
from numpy import vstack
# creating 1st array
a1=array([1,2,3])
#creating 2nd array
a2=array([4,5,6])
# creating 3rd array
a3=array([7,8,9])
# vertical stack
a4=vstack((a1,a2,a3))
print(a4)
print(a4.shape)

from numpy import array
from numpy import hstack
# creating 1st array
a1=array([1,2,3])
#creating 2nd array
a2=array([4,5,6])
# creating 3rd array
a3=array([7,8,9])
# creating horizontal stack
a4=hstack((a1,a2,a3))
print(a4)
print(a4.shape) #(9, )
###################### END ############################











