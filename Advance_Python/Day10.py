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
try:
    numerator=50
    denom=int(input("Enter the denominator: "))
    questient=numerator/denom
    print(questient)
    print("Division perform succcessfully!")
except ZeroDivisionError:
    print("Oh this is divide by ZERO error. not allows")
print("OUTSIDE try....except block")
############################################
