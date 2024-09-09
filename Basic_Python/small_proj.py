# creating a password with the help of 
# user (taking nouns and adjectives) and hiding the password

import string
# taking the 7 nouns from the user and store into nouns list
nouns=[]
for i in range(0,7):
    i=input("Enter the nouns:\n")
    nouns.append(i)

# taking the 7 adjective from user and store into adjective list
adjectives=[]
for i in range(0,7):
    i=input("Enter the adjectives:\n")
    adjectives.append(i)
    
import random # import random module for accessing the all function 
noun=random.choice(nouns)
# Here we can choice random nouns given by the user
adjective=random.choice(adjectives)
# Here we can choice random adjectives given by the user

number=random.randrange(0,50)
# We have to use the number between 0 to 50
special_char=random.choice(string.punctuation)
# string punctuation function use all special charater
password=noun+adjective+str(number)+special_char
# Generating the password
print(password) # Show the password created
########## HERE WE HAVE SUCCESSFULLY CREATE A PASSWORD ###########
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
password=noun+adjective+str(number)+special_char
for pass1 in hide(lengths(password)):
    print(pass1,end='')
######### HERE THE PASSWORD WAS SUCCESSFULLY HIDE ##############
############################ END #######################