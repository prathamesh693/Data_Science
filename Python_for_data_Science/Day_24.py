# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:10:00 2024

@author: ratho
"""
''' when we have to give an review at that time multiple
choise are there all of that we want to choose only one
other are zores
So, in that condition we will use sparse matrix
'''
# sparse matrix
# space complexity will be more in such a matrix
from numpy import array
from scipy.sparse import csr_matrix
# creating dense matrix
a=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(a)
# convert to sparse matrix (CSR method)
s=csr_matrix(a)
print(s)
#reconstruct dense matrix
b=s.todense()
print(b)
###################################
# Matplotlib
'''
Data scientist are work with all types of plots
like, barplot, histogram,boxplot etc.
matplotlib and seaborn both functionality are same.
Seaborn has better graphics than matplotlib

'''
# to draw a line
import matplotlib.pyplot as plt
x=range(1,50)
y=[value*3 for value in x]
print("Value of x:")
print(*range(1,50))
''' this is equal to 
i in range (1,50):
    print(i,end=' ')
'''
print("value of y(thrice of x):")
print(y)
#plot lines and or markers to the axes
plt.plot(x,y)
# set the x axis label
plt.xlabel('x-axis')
# set the y axis label
plt.ylabel('y-axis')
# give title to the graph
plt.title('Draw line')
# display the figure
plt.show()
# draw a line using 
# given input to x-axis and y-axis
# also given as title
import matplotlib.pyplot as plt
# x-axis value
x=[1,2,3]
# y-axis value
y=[2,4,1]
# plot lines 
plt.plot(x,y)
# set x-axis label
plt.xlabel('x - axis')
# set y-axis label
plt.xlabel('y - axis')
# set a title
plt.title('Sample graph')
# display the figure
plt.show()
################################
# write a program to plot two or more line
# with sutavle legends of each
import matplotlib.pyplot as plt
#line one point
x1=[10,20,30]
y1=[20,40,10]
# line two point
x2=[10,20,30]
y2=[40,10,30]

plt.plot(x1,y1,label='line 1')

plt.plot(x2,y2,label='line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two line graph with legend!")
plt.legend()
plt.show()
##########################
import matplotlib.pyplot as plt
#line one point
x1=[10,20,30]
y1=[20,40,10]
# line two point
x2=[10,20,30]
y2=[40,10,30]

plt.plot(x1,y1,color='blue',linewidth=3,label='line 1')

plt.plot(x2,y2,color='red',linewidth=5,label='line 2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two line graph with differ weidth and color")
plt.legend()
plt.show()
## write a program to plot two with differ syle
import matplotlib.pyplot as plt
#line one point
x1=[10,20,30]
y1=[20,40,10]
# line two point
x2=[10,20,30]
y2=[40,10,30]

plt.plot(x1,y1,color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')

plt.plot(x2,y2,color='red',linewidth=5,label='line2-dashed',linestyle='dashed')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two line graph with differ weidth and color")
plt.legend()
plt.show()

