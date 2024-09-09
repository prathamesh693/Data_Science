car ={
      "Brand": "ford",
      "model": "mustang", 
      "year": 1964}
# assign the value of key function into the x variable
x= car.keys()
print(x)
# add the keys and values into the dictionary 
car["colour"] = "white"
car # we can access the dictionary without usng print
# also use print statement
x=car.keys()
print(x)
# removing the element from the dictionary 
# the pop of dict is required the keys of the dictionary 
# but otherhand the list required the index of the element
car.pop("colout") # both the keys and values are remove
car 
# Acccessing the keys in the dictionary
# Using for loop
for x in car:
    # it will give all keys from the dictionary
    print(x)
    # it's give an error because round bracess
    #print(car(x))
    # we can use [] bracess
    print(car[x])
    
# it will you for incoding
# if you want to access both keys and value
## very important
for key,value in car.items():
    # %s is the format specifier
    print("%s == %s" % (key,value))
    # alternate printing option
    print(f"{key}=={value}")
    
# copy dictionary 
car
var =car.copy()
var
# another way to make a copy is to use the dict() function 

thisdict = {
    "brand": "ford",
    "model":"mustang",
    "year":1964
    }
dict1 = dict(thisdict)
print(dict1)

# nested dictionary
# we can create the dictionary inside the dictionary

our_family={
    "child":{
        "name":"Ram",
        "dob":"21-05-2008"
        },
    "child2":{
        "name":"sham",
        "dob":"01-01-2008"},
    "parent":{
        "name":"Vijay",
        "Dob":"01-10-1978"
        }
    }
print(our_family)
# clear() function to delete all the keys and value from the dictionary
car.clear()
print(car)
# fromkey
# create a dictionary with 3 keys, all with 
# this is the key for dictionary
x={"ram","sham","rohan","jay"}
# this is the values for dictionary
y=0
thisdictionary = dict.fromkeys(x,y)
thisdictionary
# all values of keys is 0

# get() : to get the values of dictionary
car ={
      "Brand": "ford",
      "model": "mustang", 
      "year": 1964}
car.get("model")

# items() return the dictionary's key-value
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.items()

# values():display all the values of dictionary
car ={
      "Brand": "ford",
      "model": "mustang", 
      "year": 1964 
      }
car.values()

# update(): Insert an items to the dictionary
# it can update the element in last of dictionary
car ={
      "Brand": "ford",
      "model": "mustang", 
      "year": 1964
      }
car.update({"colour":"white"})
print(car)
##################################################################################
'''  break Statement
In the break statement if the conditionis satisfied then 
the loop is terminated 
'''
# using for loop
fruits=["apple","banana","cherry","mange","kiwi"]
# we can't use range fuction in for loop it will give an error
# because range is int data type and our range is in dictionary 

for i in fruits:
    print(i)
    if(i=="cherry"):
    # after the printing the cherry then the loop will be terminated
        break
print("Thank You")

for i in fruits:
    if(i=="cherry"):
        break
    print(i)
    
''' continue statement 
in continues statement if the condition is satisfied then
skips the values and print all the element
'''
fruits=["apple","banana","cherry","mange","kiwi"]
for x in fruits:
    if x == "cherry":
        continue
    print(x)
##########################################################################################
#using range function find odd number
for i in range(1,20,2):
    print(i)
    
# nested loop 
colours = ["green", "yellow","red"]
fruits = ["guava", "banana","apple"]
for x in colours:
    for y in fruits:
        print(x,y)     
##############################################################################################
# prepare in deep list and dictionary

''' function 
 A function without argument
 '''
def my_function (): # define the function 
    print("Hello frim a function")
    
my_function() # function call
# function with arguments 
def my_function(name):
    print("hello"+name)
my_function("prathamesh")
''' when the function you can pass two or more argument is 
called as positional arguments function 
'''
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("prathamesh","jadhav")
###########################################################################
''' arbitrary arguments, *args
if you do not know how many argument that you
will be passed into your function,
add a * before the parameter name
the function definition.
'''
def my_function(*kids):
    print(kids[0]+" "+kids[2])
    # it is use 
my_function("hello","world","india")
############################################################################

''' we use the name kwargs
with the double star.
the reason is that the double star allows 
to access the keys and value from the dictionary .

as being a dictionary that maps each keyword
to the value that we pass alongside it.
that is why when we iterate over the kwargs 
there doesn't seem to ve any order 
in which they wew printed out.
add two asterisk: ** before the parameter name'''

def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myfun(first="papalala", mid="mohanlal", last="Goyal")

# if we call the functio without argument,
# it uses the default value
''' in this type of function 
if we can't provide any argument to the function then
by default value will be print
but if you give any value to the function then 
that value will be print'''

def myfunc(country = "Norway"):
    print("I am from "+country)
    
myfunc("Sweden") 
myfunc("India")
myfunc()

# passing list as an arguments
# you can send anyt data types of argument to a function 

fruits=["orange","banana","guava"]
def myfunction(fruits):
    for x in fruits:
        print(x)
    # it can give an output in the form of list
    print(fruits)
myfunction(fruits)
#######################################################################################
# Return values 
# to let a function return a value, use the return statement
def myname(x):
    return x*5+3 
# return function can direct give an output without print statement
myname(2)

# Pass Function
# if we write an abstract function then we give an empty function
# in such a case pass function will be use
def myname1():
    pass
# having an empty function definition 
# and we can't give any argument to the pass function
# myname1(2) --error
myname1()

# factorial of a number is the product of all the integer
# from 1 to that number.
def fact(x):
    if x==1:
        return 1
    else:
        # Recursive function
        # function inside the function i.e. fact
        return(x*fact(x-1))
fact(3)
fact(6)
########################################################################################
'''a lambda function is a small
 if we can avoid space complexity then use the lambda function
 without giving any primary memory
because of that the execution time is less'''
'''also called as anonymous function
a lambda fuction can take any number of arguments
but can only have one expression'''
###******* for interview it is important ***********####

def add(a):
    sum =a+10
    return sum
add(20)

# single argument using lambda function
add=lambda a:a+10
print(add(20))
# multiple argument using lambda function
add=lambda a,b: a+b+10
print(add(20,1))
''' syntax of lambda function
function_name "=" lambda keyword then arguments = opration 
then 
print statement you provide the values of an argument 
'''
###################################################################################
# finding odd number from the list using lambda function
lst =[34,12,24,53,64,13]
odd_lst=list(filter(lambda x:(x%2 !=0),lst))
print(odd_lst)
# the function filter accepts two arguments in python
# a function and an iterable such as list.
# if we use an iterable then we use an filter function

# the function is called for every item of the list 
# and a new iterable or list is returned that holds just
# those element that returned true when supplied to the list

# for even number 
lst =[34,12,24,53,64,13]
even_lst=list(filter(lambda x:(x%2 ==0),lst))
print(odd_lst)
###########################################################################################

lst1=[2,5,3,6,8,9,11,12,13,15]
# use of map function 
sqr_list=list(map(lambda x:(x**2),lst1))
# sqr_list=list(map(lambda x:(x*x),lst1))
print(sqr_list)
