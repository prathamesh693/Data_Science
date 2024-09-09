print("Hello World,\n""My name is Prathamesh Suresh Jadhav")

"""
Basic Data Type in Python

1) int
2) float / double
3) char
4) complex

"""

# int data type example
integer_value = 25
print(integer_value)
print(type (integer_value))

# float data type example
floating_value = 56.5
print (floating_value)
print(type(floating_value))

# char data type Example
char_value = 'a' # Single charactor 
print(char_value)
print(type(char_value))
char_String = "Prathamesh"
print(char_String)
print(type(char_String))

# Complex data type Example
com_num = 2+3j
print(com_num)
print(type(com_num))

"""
Type casting in python 
1) String to Integer
2) Floating to Integer
3) Integer to Floating 
4) String to Floating 
5) String to Boolean 
"""
# User Input in Python
# By default is in String Type

age = input ("Please Enter your age ")
print(type(age))
print(age)
########################################################
# String to Integer
#Type casting String to Integer (int)
num1 = int(input("Please Enter your 1 number"))
print(type(num1))
print(num1)

num2 = int(input("please Enter your 2 number"))
print(type(num2))
print(num2)

#addition of two integer
add = num1 + num2 # We can add two Integer 
print(type(add))
print(add)
#####################################################
"""floating point numbers
Interchangeble type casting
"""
# Integer to Floating conversion
value = 152
float_value = float(value)
print(type(float_value))
print(float_value)
####################################################
# String to Floating Conversion
Str1 = '25.1'
value1 = float(Str1) 
print(type(value1))
print(value1)
####################################################
# String to Floating in string as Alphabets
# Can't convert such a value
""" str2 = 'a'
cast = float (str2)
print(type(cast))
print(cast)
"""
###################################################
# Complex number
c1 = 1
c2 = 2j
print('c1:', c1 ,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
####################################################
# Boolean Values
# It can be only be one of True or False
all_ok = True
print(all_ok)
all_ok = False
print (all_ok)
print(type(all_ok))
####################################################
# You can convert String to Boolean
Status = bool(input("Ok it is confirmed?: "))
# If we can give the Input it will show True
# But we can't give any Input it will show False
print(Status)
print(type(Status))
####################################################
"""Arithmetic Operation
1) Addition 
2) Substraction
3) Multiplication
4) Division
5) Modulus
"""
# Addition of Two Integer 
home = 12
away = 14
add1 = home + away
print(type(add1))
print(add1)
#Substraction of two Integer
sub = home - away
print(type(sub))
print(sub)
# Multiplication of Two Integer
mul = home * away
print(type(mul))
print(mul)

# Division of Two numbers
div = home/away
print(type(div))
# The type is floating
print(div)
# Ans is 0.85714

# Modulus of two number
module = home%away
print(type(module))
# The type is Integer
print(module)
# Ans is 12

#Floar Division
print(100/24) # the value is in float i.e. 4.166
print(100//24) # the value is in int i.e. 4
""" But what if you are only interested in the remainder 
part of a division, the integer division operator has lost that?
well in that case you can use the modulas operation%
"""
