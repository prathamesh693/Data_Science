# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:58:07 2024

@author: ratho
"""
''' 1.Write a Python function that takes two lists and 
returns True if they have at least one common member.'''

def common_member(list1,list2):
    first=set(list1)
    second=set(list2)
    if first(list1)==second(list2):
        return bool(True)
"""   for i in list1:
        for j in list2:
            print('hello')
        if list1(i)==list2(j):
            print("True")
                """
list1=[]
list2=[]
for i in range(5):
   list1=int(input("enter first list: "))
for j in range(5):
    list2=int(input("enter second list: "))

#################################################################
''' 2.Use list comprehension to construct a new list but 
add 6 to each item.'''


#################################################################
''' 3.Write a Python program to reverse a string.'''
string_name="Prathamesh"
my=string_name[-1:-11:1]
print(my)


################################################################3
''' 4.Write a Python program to iterate over 
dictionaries using for loops.'''


##############################################################
''' 8. Write a Python program to filter a list of integers 
using Lambda. Original list of integers: 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Even numbers from 
    the said list: [2, 4, 6, 8, 10] Odd numbers from the said 
    list: [1, 3, 5, 7, 9]
'''
list3=[1,2,3,4,5,6,7,8,9,10]

####################################################33
# 9. Write a Pandas program to create the specified columns and rows from a given data frame.
''' import pandas as pd
pd.labels
pd.DataFrame(name: ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh'] 
score: [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19] 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1] 
qualify: ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])'''
##################################################################
# 10. Define a array data = array([11, 22, 33, 44, 55]) 
#  and slice it from 1 to 4
data=([11,22,33,44,55])
data[0:4]
#########################################
import numpy as np
data=np.array([1,5,6,7,0,8])




















#################################################################