# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:08:38 2024

@author: ratho
"""
''' 100% (PYTHON FOR DATA SCIENCE)
1.PANDAS -- 70%
2. NUMPY -- 20%
3.MATPLOTLIB -- 10%(USE IN EDA)
'''
#######################################################
# draw a line and use marker to mark the line 
# marker's can be cirle, triangle etc.
import matplotlib.pyplot as plt
# x axis values 
x=[1,4,5,6,7]
y=[2,6,3,6,3]

#plotting the point
plt.plot(x, y, color='red', linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue', markersize=12)
# Set the y-limits of the current axes.
plt.ylim(1,8)
# Set the x-limits of the current axes.
plt.xlim(1,8)

#naming the axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Display Marker')
plt.show()

## Use python to display a bar chart 
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color="blue")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+ "Worldwide, Oct 2017 compared to a yera ago")
plt.xticks(x_pos,x) # verticle graph 

# turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='dashed',linewidth='0.5',color='red')
plt.show()
########### HORIZONTAL GRAPH #############
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color="green")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+ "Worldwide, Oct 2017 compared to a yera ago")
plt.yticks(x_pos,x) # verticle graph 

# turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='dashed',linewidth='0.5',color='red')
plt.show()
########## give an different color to each graph
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['red','black','green','blue','yellow','cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+ "Worldwide, Oct 2017 compared to a yera ago")
plt.xticks(x_pos,x) # verticle graph 

# turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='dashed',linewidth='0.5',color='red')
plt.show()
##### By default it give an blue color to all graph
#######################################################
# To draw a HISTOGRAM 
import matplotlib.pyplot as plt
blood_sugar = [113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8) # bydefaul no. of bins is set to 10
plt.hist(blood_sugar,rwidth=0.5,bins=4)
''' histogram show normal, pre-diabetic and diabetic patients distribution
    80-100: Normal
    100-125:pre=diabetic
    125 onwords: diabetic patient
'''
plt.xlabel("Sugar level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar,bins=[80,100,125,150], rwidth=0.95, color='green')
#--------------------------------------------------------------------
# BOXPLOT
import matplotlib.pyplot as plt
import numpy as np
# creating dataset 
np.random.seed(10)
data=np.random.normal(100,20,200)

fig=plt.figure(figsize=(10,7))
# creating plot
plt.boxplot(data) # normal box plot
#show plot
plt.show()

np.random.seed(10)
data1=np.random.normal(100,10,200)
data2=np.random.normal(90,20,200)
data3=np.random.normal(80,30,200)
data4=np.random.normal(70,40,200)

data=[data1,data2,data3,data4]

fig = plt.figure(figsize=(10,7))
# creating axes instance
ax = fig.add_axes([0,0,1,1])
#creating plot
bp = ax.boxplot(data)
# show the data
plt.show()










