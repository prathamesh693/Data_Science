# Power Operator 
a = 2
b = 5
print(a**b) # 2 to the power 5 i.e. 32
###############################################################
# Assignment Operators
""" these assignment operators are referred to 
as compound operators as they combine together a numeric open
(such as add) with the assignment operator.
for wxample, the += compound operator is a 
combination of the add operator and the = operator """

x = 3
x
x+=1 # Has the same as X=X+1
x
###############################################################
# None Type has a single value none
# can't return any thing because it none
winner = None
print(winner is None)
winner
print(type(winner))
# Alternatively you can also write:
print(winner is not None)
print(type(winner))
###############################################################
""" Flow of control using If Statement
Comparison Operators
1) >  greater than
2) <  less than
3) >= greater than equal to 
4) <= less than equal to 
    
"""
# now let us give the indentation 
num = int(input("Enter the num:"))
if num > 0:
    print(num)
    
# else in an if statement 
num = int(input("Enter the no:"))
if num < 0:
    print("It's is negative number")
else:
    print("It's is positive number")

''' the use of elif statement 
in that stament we want to add more condition and 
if the first condition is satisfied then also 
compiler have to checked all condition in that case
we use elif statement 
'''
savings = float(input("enter how much you have in savings: "))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("well done")
elif savings < 1000:
    print("Thats a tidy sum")
elif savings < 10000:
    print("Welcome Sir!")
else:
    print("Thank You!")
#########################################################
'''
    Intepolation / Looping
while loop it's give true if the statement is satisfied
'''
count = 1         # Initialization of the loop
print("Starting")
while count<=10:  # Condition for the loop
    print(count)  # Print statement/ fields for the loop
    count+=1      # Incrementing of loop by one 

# For loop
print("Print out values in a range")
for i in range(2,13):
    print(i)
    print('done')

print("Only print code if iteration is present in that variable")
num = int(input('Enter a number to check for: '))
for i in range(0,10):
    if i == num: # if i is equal to num then break the condition
        break
    print(i)
print('done')
#############################################################
# now use an 'anonymous' loop variable
# it is use to avoid time comlexity
# it doesn't allocated any memory this variable
for _ in range(0,10):
    #print('.') # it will print the . is coloumn or horizontal
    print('.',end ='') # it will print the .  in rows or verticle
    print() # it will give horizontal and space between them
''' print the . in between the range and 
 it will end with the space in between end condition
'''