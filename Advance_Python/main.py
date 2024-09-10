#################################
# BEFORE USE THIS CODE first check the wrapper library is imported or not
# if not then try

# pip install wrapper
#################################
# modular programing in python

''' advantage of modular is reusability
also create a module and use it function 
but the created moodule file will be same directory
then you can access it.
because of use the user define module then 
the complexity of code is reduce.
'''

from wrapper import time_it

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
##############################