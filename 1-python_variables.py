# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:35:03 2024

@author: Admin
"""

##$$VARIABLES$$##

#####################################
fruits = ["Akash", "Pankaj", "Chetak"]
x, y, z = fruits
print(x, y, z)


########################################
##In the print() function, you output multiple variables, separated by a comma:
x = "Akash"
y = "Bhausaheb"
z = "Dhokchaule"
print(x, y, z)

##########################################
##You can also use the + operator to output multiple variables:
x = "Akash "
y = "Bhausaheb "
z = "Dhokchaule"
print(x+y+z)

######################################
##The best way to output multiple variables in the print() function is to separate them with commas,
##which even support different data types:
x = 5
y = "John"
print(x, y)

#####################################

##GLOBLE VARIABLE##
##Create a variable outside of a function, and use it inside the function

X = "AKASH"

def my_fun():
    print("My Name is",X)
    
my_fun()

###Create a variable inside a function, with the same name as the global variable

x = "Akash"

def my_fun():
    x = "Dhokchaule"
    print(x)
    
my_fun()

print(x)

##################################
##Create a variable inside a function, with the same name as the global variable

x = "Akash"

def my_fun():
    global y
    y = "Dhokchaule"
    print(x)
    
my_fun()
print(y)

#######################################
