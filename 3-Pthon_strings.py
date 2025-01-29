# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:51:50 2024

@author: Admin
"""
###################################################
##PYTHON STRING

##Strings are Arrays
A = "Akash Dhokchaule"
print(A[4])

##################################
##Looping Through a String
for x in "banana":
  print(x)

#######################################
##String Length
a = "Hello, World!"
print(len(a))

##########################################
##Check String

txt = "The best things in life are free!"
print("free" in txt)

############################################
##Check String####

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
###
###Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
##############################################
###Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

###Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")    

#############################################
####SLICING

b = "Hello, World!"
print(b[2:5])

##Slice From the Start
b = "Hello, World!"
print(b[:5])

##Slice To the End
b = "Hello, World!"
print(b[2:])

##Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

##############################################
##Python - Modify Strings##

##Upper Case
a = "Hello, World!"
print(a.upper())

##Lower Case
a = "Hello, World!"
print(a.lower())

##Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

##Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

##Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

######################################################
##Python - String Concatenation##

##Merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)

########################################################
##String Format
##we can combine strings and numbers by using f-strings

age = 21
txt = f"My name is Akash, I am {age}"
print(txt)

#####################################################
##Placeholders and Modifiers

txt = f"The price is {20 * 50} dollars"
print(txt)

####################################################
###SRING METHODS##
##first character is upper case,

##capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#######################
##Make the string lower case:
##casefold()
##This method is similar to the lower() method, but the casefold() method is stronger, 
# more aggressive, meaning that it will convert more characters into lower case, and
# will find more matches when comparing two strings and 
# both are converted using the casefold() method.

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)



##for other methods related to the string 
###https://www.w3schools.com/python/python_strings_methods.asp
##follow link
##################################################

























































