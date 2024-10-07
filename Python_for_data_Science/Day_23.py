# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:08:40 2024

@author: ratho
"""
from numpy import array
#define array
data=array([11,22,33,44,55])
# index data 
print(data[5])
#IndexError: index 5 is out of bounds for axis 0 with size 5
#Prepare a document for errors 
data=array([
    [11,22],
    [33,44],
    [55,666]])
print(data[0,]) # access all the values of 0th index
# [11 22]

# Slice a one dimensional array
# define array
data=array([11,22,33,44,55])
print(data[1:4])
# negative slicing
print(data[-2:]) # 44 55

# split input and output data
# define array
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#separate data
''' To separate the data we will use slicing
consider one table contains features and label of animal
we have to send the feature and according to that
which animal is it to the machine learning algorithms
here are the example:
X-only features and y-labels
'''
X, y=data[:, :-1],data[:, -1]
''' 1st slicing data will give us the features 
and 2nd will give us the label of the data
(generally last column)
'''
print(X)
print(y)
#################################
# broadcast scalar to one-dimensional array
# define array (vector)
a=array([1,2,3])
print(a)
# define scalar
b=2
print(b)
# Broadcast scalar with vector
c=a+b # here we can add scalar to each element of vector
print(c)
################
# Vector add
# Vector sub
# Vector L1 norm
#Define L1 
''' Vector L1 norm 
the L1 norm is caluculated as the sum of the absolute
vector values, where the absolute value of a scalar uses
the notation|a1|.
In effect , the norm is a calculation of the manhattan 
distance from the origin of the vector space.
||v||1 = |a1| + |a2| + |a3|
'''
from numpy import array
from numpy.linalg import norm
# define vector
a=array([1,2,3])
print(a)
#calculate norm
l1 = norm(a,1) # this syntax is change only both l1&l2
print(l1)
#Define L2 norm
''' The notation for the L2 norm of a vector
x is ||x||
To calculate the L2 norm of a vector,
take the square root of the sum of the 
squared vector values.
Another name for L2 is norm of a vector
is Euclidean Distance.
This is often used for calculating the error in 
machine learning models'''
from numpy import array
from numpy.linalg import norm
# define vector
a=array([1,2,3])
print(a)
#calculate norm
l2=norm(a) # it give square addition 
            # of value then root of output=3.741657
print(l2)
####################################
''' triangular matrices use in image processing 
'''
from numpy import array
from numpy import tril
from numpy import triu
# define square matrix
m=array([
    [1,2,3,],
    [1,2,3],
    [1,2,3]])
print(m)
#lower triangular matrix
lower = tril(m) # function for lower matrix
print(lower)
''' Output:
[[1 0 0]
 [1 2 0]
 [1 2 3]]
'''
# upper triangular matrix
upper = triu(m) # function for upper matrix
print(upper)
''' Output:
[[1 2 3]
 [0 2 3]
 [0 0 3]]
'''
# diagonal matrix
from numpy import array
from numpy import diag
# define square matrix
m=array([
    [1,2,3,],
    [4,5,6],
    [7,8,9]])
print(m)
# diagonal triangular matrix
diag_mat=diag(m)
print(diag_mat) # it can give [1 5 9] the diagonal
# Create diagonal matrix from vector
d=diag(diag_mat)
print(d)
'''
[[1 0 0]
 [0 5 0]
 [0 0 9]]
'''
# identity matrix
# in this matrix all diagonal are 1
from numpy import identity
I=identity(3) # identity (4) parameter are no. of col and row
print(I)

# orthogonal matrix
from numpy import array
from numpy.linalg import inv
# define matrix
Q=array([
    [1,0],
    [0,-1]])
print(Q)
# inverse equivalence
V = inv(Q)
print(V)
# transpose of matrix
c=Q.T
print(c)
# identity equivalence
I=Q.dot(Q.T)
print(I)















