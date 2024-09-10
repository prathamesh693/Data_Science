"""
Created on Wed Mar 27 08:12:58 2024

@author: ratho
"""

''' need of decorator / wrapper function in python
# interview important

'''
import time

def calc_sqr(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f'Total time for execution square is {total_time}')
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f'Total time for execution square is {total_time}')
    return result

array=range(1,100000)
out_square = calc_sqr(array)
out_cube=calc_cube(array)
################################################
def say_hi():
    return "prathamesh"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorator = uppercase_decorator(say_hi)
print(decorator())
#############################################
# for us to apply decorators we simply use the @ symbol before the function we'd like to decorate.

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
# for us to apply decorators we simply use the @ symbol 
# before the function we'd like to decorate.
@uppercase_decorator
def say_hi():
    return "prathamesh"
say_hi()
##########################################
# applying multiple decorators to single function
def split_string(function):
    def wrapper():
        func=function()
        split_decorator=func.split()
        return split_decorator
    return wrapper
''' in various time we have to decorate one function multiple time
in that cases use the multiple decorators
@@@@@ we aslo use more decorating function 
'''
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
''' here we will call split_string function first and then 
uppercase_decorator
i.e. first the string will be split and then it will be uppercase'''
@split_string
@uppercase_decorator

def say_hi():
    return "brat uchiha evil"
say_hi()
'''         step for decorate function
1. write a  decorating function i.e.(split_string etc.)
2. call that function using @ 
3. define the function you want to decorate
4. and call that function
'''
#############################################
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f' took \n{total_time}mili sec')
        return result
    return wrapper

@time_it
def calc_sqr(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square = calc_sqr(array)
out_cube=calc_cube(array)
##################################
# modular programing in python
''' advantage of modular is reusability
also create a module and use it function 
but the created moodule file will be same directory
then you can access it 
'''
###########################################################################################