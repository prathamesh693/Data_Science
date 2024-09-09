
# Program to roller coaster and pop-corn shop
print("Welcome to the rollar coster!")
height =int(input("please enter your height in cm: \n"))
if height>=120:
    print("you are eligible for roller coaster")
    age=int(input("enter your age in years: "))
    bill=0
    if age<12:
        print("child's ticket is 5$\n")
        bill=5
    elif(age<=18 and age>=12):
        print("Adult's ticket is 20$\n")
        bill=20
    elif(age<=40 and age>=19):
        print("Younger's ticket is 25$\n")
        bill=25
    else:
        print("Elder's citizen ticket is 15$")
        bill=15
    print("Are you want to Pop corn. y or n: ")
    choice=input()
    if choice=='y':
        print(""" Enter your favariote pop corn
              1) Masala Popcorn
              2) Normal Popcorn
              3) Cheese Popcorn
              4) Other's""")
        choose=int(input(":-"))
        if choose==1:
            print("The price of masala Popcorn is: 10$")
            bill+=10
            print(f"The total bill is :{bill}$")
        elif(choose==2):
            print("The price of Normal Popcorn is: 5$")
            bill+=5
            print(f"The total bill is :{bill}$")
        elif(choose==3):
            print("The price of cheese Popcorn is: 15$")
            bill+=15
            print(f"The total bill is :{bill}$")
        else:
            print("Sorry!")
            print("The Popcorn you want are not in shop!")
            print(f"The total bill is :{bill}$")
    else:
        print("Thanks for your consideration!")
else:
    print("your are not eligible for rollar coaster!")
######################################################################################
# calculate BMI in meter
height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is :{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"You are normal weight and your BMI is :{BMI}")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is :{BMI}")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is :{BMI}")
else:
    print(f"You are clinically obese and your BMI is :{BMI}")

##########################################################################################
# calculate BMI in centimeter
height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
BMI=round((weight/((height/100)**2)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is :{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"You are normal weight and your BMI is :{BMI}")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is :{BMI}")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is :{BMI}")
else:
    print(f"You are clinically obese and your BMI is :{BMI}")

##########################################################################################
# To find the duplicate of the list
# Important for Interviews question 
'''if the lst is not sorted then first sort it and 
then compare it.
if you not use sorted list then it will give you 
incorrect output.
'''
lst2=[1,3,2,4,5,2,9,8]
lst2.sort()
print(lst2)
def is_duplicate(lst2):
    for i in range(len(lst2)-1):
        # to compare current number with next number
        if(lst2[i]==lst2[i+1]):
            return True
    return False
print(is_duplicate(lst2))
#################################################################################################
# program to write a leap year
def is_leap(year):
    if((year>0) and (year%4==0) and (year%100!=0) and (year%400==0)):
        return True
    return False
is_leap(2000)

# Leap year
def isleap(year):
    if(year>0 and year%4==0):
        return True
    return False
isleap(2024)

# Mario pyramid
# interview important question 

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
    
    for i in range(4):
        for j in range(i+1):
            print("#",end=" ")
        print()
        
        for i in range(4):
            for j in range(4-i):
                print("#",end=" ")
            print()

# Write a code for diamond printing
for i in range(0,4):
    for j in range(i+1):
        print("#",end=" ")
    print() 
for i in range(0,4):
    for j in range(8-i):
        print("#",end=" ")
    print()

#################################################################
# find the min-max values using function
lst=[21,2,56,3,13,48,4,9,86,32,12,15,17]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("The minimum value",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("The maximum value is:",max)

print(min_max(lst))
##############################################################################
# is palindrome 
# if the string are in reversed the it show the true 
# othervise false

def is_palindrome(input):
    if input==" ":
        print("wrong input given Please check it again...")
    # elif(input==input[::-1]):
        # print("The string is already reversed...")
    else:
        print("The reverse string is:")
        string=input[::-1]
        if string==input:
            return True
    print(string)
    return False
string="pratham jadhav"
is_palindrome("pratham jadhav")

# 
users=["admin","manager","employee","staff","worker"]
for user in users:
    if user=="admin":
        print("Welcome! You are an admin")
    elif(user=="manager"):
        print("Welcome! you are an manager")
    elif(user=="employee"):
        print("Welcome! you are an employee")
    elif(user=="staff"):
        print('Welcome! You are the staff')
    elif(user=="worker"):
        print("Welcome! you are the worker")
    else:
        print("You entered the wrong Password!!")
        print("Please check it again....")
############################################################
print("Enter who you are...!!")
users=input("admin\nmanager\nemployee\nstaff\nworker\n:- ")
if users=="admin":
    print("Welcome! You are an admin")
elif(users=="manager"):
    print("Welcome! you are an manager")
elif(users=="employee"):
    print("Welcome! you are an employee")
elif(users=="staff"):
    print('Welcome! You are the staff')
elif(users=="worker"):
    print("Welcome! you are the worker")
else:
    print("You entered the wrong Password!!")
    print("Please check it again....")
###############################################################
#to create a random password
import string
# list of adjectives
adjectives =["sleepy","slow","smelly","wet","fat","era"]
# list of noun
nouns=["apple","dinosaur","ball","duck","pandas","hammer"]
# pick the words
import random

adjective = random.choice(adjectives)
noun = random.choice(nouns)

# select a number
number= random.randrange(0,100)
# select a special charater
# punctuation function can give an all special type charater
special_char=random.choice(string.punctuation)
# create a new secure password
password=adjective+noun+str(number)+special_char
print("the new password is:%s"%password)

# create multiple password using while loop

while(True):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    # select a number

    number= random.randrange(0,100)
    # select a special charater
    # punctuation function can give an all special type charater
    special_char=random.choice(string.punctuation)
    # create a new secure password
    password=adjective+noun+str(number)+special_char
    print("the new password is:%s"%password)
    hii=input("you want to create other password? Y or N: ")
    if (hii=='n'):
        break
    
