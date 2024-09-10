'''                 Advanced Python 
# Iter tools 
# impotant for interview purpose list comprehsion
''' 
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
''' we can write same method using list comprehension 
# it is code optimixation technique
# lst=[business logic]
'''
lst=[num for num in range(0,20)]
print(lst)
#################################################################################################################
names=['dada','mama','kaka']
# list comprehension logic
lst=[name.capitalize() for name in names]
print(lst)

# list comrehension with if statement 
def is_even(num):
    return num%2==0
# if statement is always write on left side of for loop/ business logic
lst=[num for num in range(10) if is_even(num)]
print(lst)

#############################################################################################################
# loop inside loop using list comprehension 
lst=[f'{x}{y}' for x in range(4)for y in range(4)]
print(lst)
''' create a k-map matrix index using for loop
lst=[f'{x}{y}' for x in range(2)for y in range(2)]
print(lst)
'''
# dictionary comprehension
# business logic i.e. x:x*x
dict={x:x*x for x in range(3)}
dict
'''              generator 
# it is another way of creating iterators in a simple way where 
# it uses the keyword "yield"
# instead of returning it in a defined function.
# generators are implementd using a function
'''
# purpose some time we want only 1,2,3 then generator logic will be use

gen=(x for x in range(3)) 
print(gen)
# it also allow to access one value at a time 
for num in gen:
    print(num)
##########################################################################################################
# for accessing particular value
gen=(x
     for x in range(3))
# the word next gives us only one value
# in only one statement we can't get random value like 1,2
next(gen)
next(gen)
# if we have to write two time next gen then it will give us the value only 1 and so no
#########################################################################################################
# function which returns multiple values
# print even values
def is_even(end):
    for num in range(0,end,2):
        # yield keyword give us multiple returns
        # in our case it is 0,2,4
        yield num
for num in is_even(6):
    print(num)
    
#########################################################################################################
# now instead of using for loop we can write our own generator
gen=is_even(6)
next(gen)
next(gen)
# the output will be 2
########################################################################################################
# chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    # the keyword hide can hide the password in this case
    for ele in itr:
        #if you are not write ele* then it will give the password but it is not hide
        yield ele*'*'

'''
"ele* appears to be a placeholder for an element from 
an iterable. the asterisk (*) is likely just a character 
used to represent a placeholder or a wildcard.
for instance, if you're iterating over a list of elements, 
"ele*" could symbolize any element in that list.
It's a generic representation that doesn't correspond to any specific syntax
in python or itertools.
'''
passwords=["My_name","Pratham","101010","@123"]
for password in hide(lengths(passwords)):
    print(password)

######################################################################################################
# creating random password and hide it
import string
nouns=['name','fame','game','view','spark','sum']
adjectives=['rahul','bala','mountain','light','one']
import random

noun=random.choice(nouns)
adjective=random.choice(adjectives)
#####@@@@@
number=random.randrange(0,50)
####@@@@
special_char=random.choice(string.punctuation)
password=noun+adjective+str(number)+special_char
print(password)

def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
password=noun+adjective+str(number)+special_char
#passwords=["My_name","Pratham","101010","@123"]
for pass1 in hide(lengths(password)):
    print(pass1,end='')
#####################################################################################
# enumerate is important for interview purpose
# also use in machine learning
lst=['milk','egg','bread']
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")

# using enumerate 
lst=['milk','egg','bread']
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
# use of zip function
# also use in machine learning
name=['dada','mama','kaka']
info=[958,5861,884645]
for nm,inf in zip(name,info):
    print(nm,inf)
    
# zip function with mismatch
name=['dada','mama','kaka','baba',]
info=[958,5861,884645]
for nm,inf in zip(name,info):
    print(nm,inf)
# it will not display excess mismatch items in name
# to avoid this output
# we use zip_longest function
from itertools import zip_longest
name=['dada','mama','kaka','baba',]
info=[958,5861,884645]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
# if the mismatch then it will show none
# but we want to set it as 0
# using the keyword fillvalue

name=['dada','mama','kaka','baba',]
info=[958,5861,884645]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
######################################################################################
# use of all() function, if all the values are strue then it will produce 
# to check the 0 value present or not in ML code
# and also remove it 
lst=[2,5,-9,6,5,-5]# value must be non zero i.e. +ve,-ve
if all(lst):
    print('The values are true')
else:
    print("There are null value")
    
##########
lst=[2,5,-9,-5,0,5]
if all(lst):
    print("The values are true")
else:
    print("There are null values")
##########
# use of any if any one non-zero values
lst=[0,0,9,-1,6,0]
if any(lst):
    print("It has some non zero values")
else:
    print("all values are zero in the list.")
# all zeros value
lst=[0,0,0,0,0]
if any(lst):
    print("It has some non-zero values")
else:
    print("All values are null in the list.")
##################################################
# count function
# in image processing it will be use
# it is also usefull ML
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

# to start for 10 
from itertools import count
counter=count(start=10)
print(next(counter))
print(next(counter))
print(next(counter))
###############################################################
# Cycle() function
# suppose you have repeated task to be done, then you
# real time application it is used
# continues monitoring/display the screen then also use 
# it is also use data syncronization
''' # it gives an infinite loop
import itertools
instructions=('eat','code','sleep')
for inst in itertools.cycle(instructions):
    print(inst) '''
    
import itertools

instructions = ('eat', 'code', 'sleep')
counter = 0
limit = 10  # Set how many times you want the loop to run

for inst in itertools.cycle(instructions):
    if counter >= limit:  # Break after reaching the limit
        break
    print(inst)
    counter += 1  # Increment counter

############################################################################################
# repeat() function 
# 
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)
###############
# permitation and combination difference search tasks for todays

# combination() function
from itertools import combinations
players=["john","joni","janardhan"]
for play in combinations(players,2):
    print(play)
###################
game=['cricket','bascket','ludo']
player=['jonh','joni','mohan','jay']
# combination of two string is possible using 
# product function 
'''
# The combinations() function expects two arguments: an iterable and 
an integer that defines the length of the combinations.
TypeError: 'list' object cannot be interpreted as an integer

for play in combinations(game,player):
    print('play')
'''
# Use product function to get all possible pairs
for play in itertools.product(game, player):
    print(play)
############################################
# permutations ()
from itertools import permutations
player=['jonh','joni','mohan','jay']
for seat in permutations(player,2):
    print(seat)
    
# product () function
from itertools import product
team_a=['rohit','pandya','bumrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)
    
############################################
'''
in python, assignment statements (ob_b=ob_a)
do not create real copies.
it only creates a new variable with the same reference.
so when you want to actual copies of mutable objects (list,dict)
and want to modify the copy without affecting the original,
you have to careful.
for 'real' copies we can use the copy module.
however, for compound/ nested objects(e.g. nesteed lists or dict)
and custom objects there is an important diff. between
shallow and deep copying.
- shallow copies : only one level deep. it create  a new copy
and populates it with references to the nested objects.
theis means modyfing a nested obj
in the copy deeper than original
-deep copies: a full independent clone. it create a new copy
and then recursively populates it with copies of the nested 
'''
# assignment operator 
# this will only create a new variable with the same reference
lst_a=[1,2,3,4,5]
lst_b=lst_a

lst_a[0]=-15
''' in this case we can only assign the values of lst_a into lst_b
if we can make any changes the assing variable values 
will be change it will copy the values it will only assign 
the values
#### it is disadvantages of assignment operator
if we make the changes in previes variable then new will be also 
change
######## and the output will be different
'''
print(lst_a)
print(lst_b)
#################################################################################################################################