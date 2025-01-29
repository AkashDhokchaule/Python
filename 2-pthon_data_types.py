
##Print the data type of the variable x:
 
x = "Akash"
y = 52
z = True
a = range(7)

print(type(x))
print(type(y))
print(type(z))
print(type(a))

######################################
##NUMBERS

##there are 3 types oF NUMBERS in python
##int, float, complex

x = 9
y = 6.099
z = 1+6j

p = -888
q = 99E454
r = -87.7e100

print(type(x))
print(type(y))      
print(type(z))
print(type(p))
print(type(q))
print(type(r))

##########################################
##TYPE CONVERSION 
###Convert from one type to another datatype:

a = 11
c = 8e2
d = 9.888

p = float(a)
q = int(d)
r = int(c)


print(p)
print(q)
print(r)

#####################################
## random() function 
##Import the random module, and display a random number between 1 and 11:

import random
x = random.randrange(1,11)
print(x)
