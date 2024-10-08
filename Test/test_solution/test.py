# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:07:34 2024

@author: ratho
"""
'''
Q1. Write a python program to print all even numbers from a 
given list of numbers in the same order and stop printing any 
after 237 in the sequence. Sample numbers list: 
    numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 
               566, 597, 978, 328, 615, 953, 345, 399, 162, 
               758, 219, 918, 237, 412, 566, 826, 248, 866, 
               950, 626, 949, 687, 217, 815, 67, 104, 58,
               512, 24, 892, 894, 767, 553, 81, 379, 843, 
               831, 445, 742, 717, 958,743, 527]
    output: []
'''
def even_No():
    list11 = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 
           566, 597, 978, 328, 615, 953, 345, 399, 162, 
           758, 219, 918, 237, 412, 566, 826, 248, 866, 
           950, 626, 949, 687, 217, 815, 67, 104, 58,
           512, 24, 892, 894, 767, 553, 81, 379, 843, 
           831, 445, 742, 717, 958,743, 527]
    list1=tuple(list11)
    
    for i in list1:
        if i%2==0 and i==237:
            print(i)
            break;
            '''
        if i<237:
            print(i)
            break;
        if i%2==0:
            print(i)'''
                
even_No()
-------------------------------------------------------------------
''' Q2. Write a python program to find a list of integers with 
exactly two occurrences of nineteen and at least three 
occurrences of five. Return True otherwise False. e.g. Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
'''
# Answer 
count2=0
count1=0
list2=[19, 19, 15, 3, 5, 5, 2]
for i in list2:
    if i==19:
        count1=count1+1
    elif i==5:
        count2=count2+1
if count1==2 and count2==3:
    print("True")
else:
    print("False")
------------------------------------------------------------------------
'''
Q3. Write a python program to find numbers that are greater 
than 10 and have odd first and last digits.
e.g: Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]'''

list3= [1, 3, 79, 10, 4, 1, 39, 62]
new=[]
for i in list3:
    if i>10 and i%2 !=0:
        new.append(i)
print(new)
-------------------------------------------------------------------
'''
Q4. Write a python program to find the largest negative and 
smallest positive numbers (or 0 if none).
e.g. Input:
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output:
[-6, 2]'''
list4 = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
list4.sort()
a=[]
new_list=[]
for i in list4:
    if i>0:
        new_list.append(i)
        break;
    if i<0:
        a.append(i)
new_list.append(a[-1])
new_list
---------------------------------------------------------------
'''
Q5. 5. Write a Python program that matches a string that has 
an a followed by zero or more b's.
'''
str1 = "pranab"
str2= "Rahul"
            
    

