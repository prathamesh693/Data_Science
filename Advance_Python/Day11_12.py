##########################

# Exception Handeling

##########################
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
class Human:
    
    def __init__(self,n,o):# constructor
        self.name=n
        self.Ocuppision=o
        
    def do_work(self):
        if self.Ocuppision=="tennis player":
            print(self.name,"plays tennis")
        elif self.Ocuppision=="actor":
            print(self.name, "shoots film")
            
    def speaks(self):
        print(self.name, "says how are you?")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

maria=Human("maria_sharapova","tennis player")
maria.do_work()
maria.speaks()
###############################################
# Inheritance in python
'''
syntax of inheritance
class class_name(base_class)
or
class child_class_name(parent_class) 

'''
# this is the base class
class vehical:
    def general_usage(self):
        print("general use: transportation!")
# subclass can inherete the base class
class car(vehical):
    
    def __init__(self):
        print("I'm car")
        self.wheel = 4
        self.has_roof = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with friends")
# again the subclass can inherite the base class
class motorcycle(vehical):
    
    def __init__(self):
        print("I'm Motorcycle") # this is written in constructor
        self.wheel = 2
        self.has_roof = False
        
    def specific_usage(self):
        self.general_usage()
        print("specific use: local communication, racing")
        
c=car()
c.specific_usage()
m=motorcycle()
m.specific_usage()
# print(issubclass(car, motorcycle))
''' this statement gives us the false because it can check the 
given class is subclass of the given class or not
if it is subclass then it will give an True otherwise False
'''
print(issubclass(motorcycle,vehical ))
# in this statement give an True because motorcycle is 
# a subclass of vehical
print(issubclass(vehical, motorcycle))
# it give False , vehical in not subclass of motorcycle
# althrow the motorcycle is subclass of vehical
########################################################
# multiple inheritance

class father:
    def skills(self):# not constructor
        print("I like garding,programming")
class mother:
    def skills(self):# not constructor
        print("I like cooking,art")
        
class child(father,mother):
    # the child can inherite both the father and mother skills
    def skills(self):
        father.skills(self)
        # call parent class into child class
        mother.skills(self)
        print("I like sports")
        
c=child()
c.skills()
################################################