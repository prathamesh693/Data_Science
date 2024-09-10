''' syntax error -
'''
''' system generated error/ runtime errors --- exception
Exception can be handel by using some function but errer are not 
handel
so... we have and error then reconstruct the code/ modify the 
code.

code generated error---- error
'''
# to handel the exception
# from os import name


try:
    numerator=50
    denom=int(input("enter the denominator: "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as Zero are not allowed.")
except ValueError:
    print("Only INTEGERS should be entered.")
##############################################
# Handling exception without naming them
''' without mentioning the type of exeception 
reponse time is less in that case
the time complexity will be more'''

try:
    numerator=50
    denom=int(input("enter the denominator "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("Only INTEGERS should be entered")
except:
    print("OOPS.....some exception raised")
###############################################
# Handling exception using try...except...else

try:
    numerator=50
    denom=int(input("enter the denominator\n"))
    quotient=(numerator/denom)
    print("Division perform successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTERGER should be entered")
else:
    # else statement shows us the value along with the statement
    print("The result of division operation is",quotient)    
###############################################
''' if our code has some exception but we want to execute the 
below statement then we will use finally functionthat
that will be execute at any cost '''

try:
    numerator=50
    denom=int(input("enter the denominator\n"))
    quotient=numerator/denom
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERs should be entered")
else:
    print("The result of division operation is", quotient)
finally:
    print("OVER AND OUT")
###########################################
### OOPs in Python
# Classes and Object in python
''' template/blueprint and combination of methods and properties 
in order to excute the class then you have to declair the object
object is called instance
## the basic OOP concepts such as encapsulation , inheritance and 
polymorphism.

syntax of class
class class_name:
    "properties name
    methods name()" i.e. data /field

## data abstraction 
-- declare the circle class, have created a new data type 
syntax of creating object
circle=circle();

'''
