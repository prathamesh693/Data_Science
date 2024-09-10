#################

# BEFORE USE THIS FILE CHECK THE pandas LIBRARY IS AVAILABLE OR NOT
# if not then try
# pip install pandas on command line
# to install pandas library

##################
# shallow copy 
# one level deep. mlodifying on level 1 does not affect
# use copy.copy()
import copy # import the copy model
lst=[2,3,5,6]
lst1=copy.copy(lst)
''' in shallow copy we can create a new copy file and 
assign to the new variable and if we have changes in new
variable value then it will not affect the original 
varuable
like that.....'''
lst1[2]=-7
print(lst)
print(lst1)
###################################
# but with nested object's modifying on level 2 and
# both the lst are changes
import copy
lst=[[2,5,8,6,3],[-5,-6,-2,5]]
lst1=copy.copy(lst)

lst1[0][0]=-1
print(lst)
print(lst1)
##################################
# deep copy
import copy
lst=[[2,5,8,6,3],[-5,-6,-2,5]]
lst1=copy.deepcopy(lst)
''' in deep copy we will use 2 level copy and the previes lst 
are not change.
'''
lst1[0][0]=-1
print(lst)
print(lst1)
################################################################################
# Real python is now begin........@@@
######################### HOW TO READ A FILE IN PYTHON #################################
import pandas as pd
''' f1=pd.read_csv('buzzers.csv') # relative path '''
f1=pd.read_csv("C:/1-Python/Advance_Python/buzzers.csv") # absolute path
print(f1)
#############################
# check for working directory
import os
with open("C:/1-Python/Advance_Python/buzzers.csv")as raw_data:
    print(raw_data.read())
#############################
# Reading CSV data as lists
import csv
with open("C:/1-Python/Advance_Python/buzzers.csv")as raw_data:
    for line in csv.reader(raw_data):
        print(line)
''' in some machine learning some time we want the data in list formate
but it present in csv form
then we will use this csv library or file will be used.'''
# Reading CSV data as dictionaries
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
######################################
with open('buzzers.csv') as data:
    # ignore=data.radline()
    flights={}
    for line in data:
        parts=line.strip().split(',')
        if len(parts)==2:
            k,v = parts
            flights[k]=v
flights
######################################
# pre-requisite to decorators
def plus_one(number):
    number1=number+1
    return number1
plus_one(4)
# Defining function inside other functions
def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    ''' in this function return will be create
    one object in this state not give an output
    '''
    result=add_one(number)
    return result
# the result will be display here or after the second 
# function end.......
plus_one(4)
#####################################
# Passing function as arguments
# to other function 
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)
######################################
# function returning other functions
def hello_function():
    def say_hi():
        return 'hi'
    return say_hi
### hello_function() # it will give us an object not an output
hello=hello_function() # so we assing the function to variable
# and then print it
print(hello_function())
######################################################################################