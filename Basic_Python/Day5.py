# Python program to find or print odd number from given range

start, end = 4,22 # The range of odd number
for num in range(start, end+1):
    # Check the condition of odd numbers 
    if num%2!=0:
        # Print the odd number in row formate
        print(num,end=" ")
        # print the odd number in column formate
        print(num)

print("\nThank you")
##############################################################
# code for even number
start, end = 3,15
for i in range(start, end+1):
    if i%2==0:
        print(i,end=" ")
print("\nThank you")
############################################################
x,y,z = 5,6,7
print(x)
print(y)
print(z)
# x,y,z = 5 
""" It can olny assign the values to x and 
it give the error"""
print(x)
print(y)
print(z)
#############################################################
''' Globle variable declaration
and function define and excute'''
x= "Awasome" # globle variable
def python_string():# function declairation
    print("Python is "+x)
python_string() # function calling
#############################################################
#globle variable and local variable
x="awesome"
def my_function():
    x="factastic"
    print("python is "+x)
    ''' the function can give priority to local variable
    than the globle variable'''
my_function()
print("python is "+x)
################################################################
#getting data type
x=5
print(type(x)) # int data type
x=range(5)
print(type(x)) # range data type
x={'myname':'prathamesh',"rollno":21}
print(type(x)) # dict data type
#############################################################
#A string can not concatinate with the other data type 
# It can concatinae with the string only
str1 = "Prathamesh"
str2 = 3
# str3 = str1+str2
# print(str3) #it give an error
########################################################
# work in data science then the slicing 
# string slicing 
'''The use of slicing 
the client asking of an address and he want only want location then use slicing
and then convert into the tabular form'''

x="This is python .It is very powerful"  
print(x[1:9])
# slicing from the starting index
print(x[:5])
# slicing to the end
print(x[5:])
# Reverse or negative indexing
y ="This is the Python Program "
print(y[-8:-5]) # negative string print
x="Hello World"
print(x[::-2])
print(x[::-1])
'''first is the range (1: )and then the 
value between turn to reverse(:-1)'''
''' in product reviews the user write their opinoion in upper and lower case
but we want it in upper case then'''
x=y.upper() #use upper function 
print(x)
x=y.lower() #use lower function
print(x)
x= "this is python"
print(x)
x=y.strip() # use strip to remove the white space from the string
# it can by default remove the left space not between the string
print(x)
x= "Hello world"
print(x.replace("world","parth"))
# use of replace function can replace the whole string
print(x.lstrip())
x= "hello world"
print(x.split(' ')) 
'''The split function use the delimeter and separate the string 
in this case the delimeter is space (" ")
we don't have any function to remove the space between the 
two string in one variable that's why we use the split function '''
################################################################
# find method for string
x= "This is the python string and python is very powerful"
print(x.find("the"))
'''it can give us the index of finding string
use ex. ram salary is 2k and sham salary is 4k
user want the salary then use find method'''
########################################################
x= "hello"
y="world"
print(x+y)
# to add white space 
print(x+" "+y)
################################################################################################
# f' string use in print statement 
x = 19
print("my name is shreyash and my age is {x}")
# it can simple string 
print(f"My name is shreyash and my age is {x}")
'''direct string with interger concatinate it will give you an 
error but if we use f string concatinate the it's possible
'''
quantity = 3
item_on = 52
price = 88
print(f'I want the {quantity} pieces and item number is {item_on} and the price is {price}')
my_order = "I want {} pieces and item number is {}, it's price is {}"
print(my_order.format(quantity,item_on,price))
# we use here the format function and passes him the values or variable that hold the value
quantity = 3
item_on = 52
price = 88
print(f'I want the {0} pieces and item number is {1} and the price is {2}')
print(my_order.format(quantity,item_on,price))
###############################################################################
''' The escape character allows you to use double quotes when 
user want some access cotted sentence 
escape character is '\  \'
'''
text="This is fun fair and it has got big\"round rigo\""
# below can give an syntax errer 
# text="This is fun fair and it has got big"round rigo""
print(text)
##############################################################################
''' operator precedence 
rule for mathematical operations 
PEMDAS
P= paranthesis 
E= Exponential
M= Multiply
D= division
A= addition 
S= substraction
'''
print(3*3+7-9/5*5+11)
#############################################################
''' Python List
usually list is data type open and close square bracess
The list items are indexed, the first item is 0th index
It can store any data type at a time 
'''
lst = ["shekhar", 20,98.5]
print(lst[0])
print(lst[2])

fruits = ["banana", "apple", "Cherry"]
fruits.append("mango") # it can add items in the list
print(fruits)
# To remove the items from the list
fruits.clear()
print(fruits)
lst2 =lst.copy()
print(lst2)
# in the list the repeated items is allowed and 
fruits= ["apple","banana", "Cherry","apple"]
print("apple")
print(fruits.count("apple")) # count function
# extend function in string
# use to concatinate two list
lst= [2,5,6]
lst1= ["prathamesh",5,2.1]
lst.extend(lst1) 
print(lst)
# insert function can add the values in particular location
# list is mutable 
fruits= ["apple","banana", "Cherry","apple"]
fruits.insert(2, "Mango")
print(fruits)
fruits.pop(2)
# To remove the value in a particular index
print(fruits)
fruits.pop() #it can by default remove last value from the list
print(fruits)

lst=["cherry", "cherry", "banana"]
lst.remove("cherry") # it can remove the first cherry
print(lst)
lst=["cherry", "cherry", "banana"]
lst.reverse()
print(lst)

list1 = ["cherry","apple","orange","banana"]
list1.sort()
print(list1)
########################################################################
# this methods are used in web scrapping
############################################################################
# Tupple
'''  tuple is denoted by ()
tuple is immutable 
'''
tup = ("cherry","cherry","banana")
print(tup)
print(tup[2]) 
# once tuple is created , you cannot change it's value
x=("apple", "banana",2,"cherry")
# x[1]="kiwi" # it can give us an error because tuple is immutabel
# first convert into list 
y=list(x)
y[1]="kiwi"
# convert it into tuple
x=tuple(y)
print(x)
# addhar no of the person we can't chage the number 
# in that case we use tuple 
# the data can't be change that is the best example of tuple
# it's also allove to mix data type

# to join two or more tuples you can use the + operator
tup1 = (1,2,5,6)
tup2 = ('a','b','c')
tup3 = tup1+tup2
print(tup3)
print(len(tup3))
###############################################################################
''' Dictionary
it is denoted by {} bracess
and the key:value pair
''' 
dict1 = {"name":"Prathamesh","class":"Sy","rollNo":20,"Year":2024}
print(dict1)
print(len(dict1))
# to access the value using the key
# and use get () function
print(dict1.get("class"))

dict2={"brand":["maruti","mahendra","Toyato\n"],"model":['a','b','c'],"year":[2011,2013,2022]}
print(dict2)
print(dict2.get("brand"))
# To get key of an dictionary
print( dict2.keys())
#################### END OF THE SESSION #######################################################