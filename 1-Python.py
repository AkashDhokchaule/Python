age = input('enter your age : ')
print(type(age))
print(age)

age1 = int(input('enter your age : '))
print(type(age1))
print(age1)

age2 = int(input('enter your age : '))
print(type(age2))
print(age2)

age=age1+age2
print(age)

int_val = 100;
string_val = '1.5'
float_val = float(int_val)
print('int val as a float : ',float_val)
print(type(float_val))
float_val = float(string_val)
print('string val as a float : ',float_val)
print(type(float_val))

#complex

c1 = 1
c2 = 2j
print('c1:',c1 ,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean Values

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

#Arithmatic Oparation

home = 10
away = 15

print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for = 10
goals_againts = 7
print(goals_for - goals_againts)  
print(type(goals_for - goals_againts))  

#########by using // operator result id generated in int formate NOT in float 
print(100//20)#result is 5
print(type(100//20))
print('modulus division 100 % 13 : ',100 % 13)
print('modulus division 3 % 2 :  ',3 % 2)


a = 5
b = 3
print(a ** b)#result 5^3=125


#############################

#Assingnment Operators
x = 0
x += 1 #same as  x = x + 1


winner = None 
print(winner is None)
print(winner is not None)

winner = None 
print('winner:',winner)
print('winner is None : ',winner is None)#N is Capital
print('winner is not None :',winner is not None)


#############################
#Comparison Operators

num = int(input('Enter the number : '))
if num > 0:
   print(num) #indentation is imp
    
num = int(input('Enter another number : '))
if num > 0:
   print(num)#to run code here block of code is require


num = int(input('Enter another number : '))
if num < 0:
   print('Its negative.')
else:
   print('Its Positive.')



#use of elif

savings = float(input('enter how much savings : '))
if savings ==  0:
    print('Sorry No savings .')
elif savings < 500:
    print('Well Done')
elif savings < 1000:
    print('Thats a Tidy sum')
elif savings < 10000:
    print('Welcome Sir ')
else:
    print('Thank You...')

#####################
#Iteration/Looping
#while Loop

count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1      
#for loop
#loop over a set of values in a rang

print('printout values in a rang')
for i in range(2,10):
    print(i)     #last value is not print/i-1 i.e result is 2 to 9
print('Done..')

###############################################

print('Only print code if all iterations completed')
num = int(input('enter the number to check for : '))
for i in range(0, 16):
  if i == num:
      break
  print(i)
print('Done.')

###############################
###use an Anonymous Loop Variables
# _ called as Anonymous Variables
#no memmory is assigned to Anonymous Variables

for _ in range(0,10):
    print(".")       #result is printed vertically
    
for _ in range(0,10):
      print(".",end="") #result is printed horizontally
      
for _ in range(0,10):
    print(".",end="")
    print()  #result is printed vertically
########################################


#variables declaearion
x,y,z = 5,6,7 #no of variables should be equale to no of values assign to variables
print(x)
print(y)
print(z)


#global variable
x = 'awesome'
def myfunction():
    print("python is "+x)
myfunction()   

#global and local variables 
x='awesome'
def myfunction():
    x='fantastic'
    print('python is '+x)
myfunction()
print('python is '+x) 
#priority is gives to local variables
###########################################

###getting datatype

x=5
print(type(x))  #int

x=range(2,3)
print(type(x))  #range

x={'name':'ram','age':33}
print(type(x))   #dictionary

x=2+3J
print(type(x)) #complex

x=2.777
print(type(x)) #float

##assigning values

str1='Hello'
str2="2"
str3=str1+str2
print(str3)
##################

x=""""this is python.it is very powerful"""
print(x)

##string slicing
x='this is python.it is very powerful'
print(x[2:8])

#slicing from start
print(x[:4])

#slicing to the end 
print(x[5:])  #from index 5 to end

#negative indexing
print(x[-5:-2])
print(x[-5:])
print(x[:-4])

###########
##string modify
#upper and lower case letters
x='this is python.it is very powerful'
x=x.upper()
print(x)
x=x.lower()
print(x)

#
x='          this is python'
print(x.strip())


#########################
x="this is python"
print(x[::-1])
print(x[::-2])

#find methods searches the string for a specified values at
x='this is python and it is very powerful'
print(x.find('and'))

#############
##string concateness
x='hello'
y=' world'
print(x+y)


#to add white spaces 
x="akash"
y="dhokchaule"
print(x+" "+y)

######string formate
x=21
print(f'my name is Anthony and my age is {x}')
#print(x+y) gives error 

######################methos-1
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and items number is {item_no} and its price is {price}")

######################method-2

quantity=4
item_no=56
price=99
my_order="I want {} pieces and items number is {} its price {}"
print(my_order.format(quantity,item_no,price))

#######################method-3
quantity=4
item_no=56
price=99
my_order="I want {0} pieces and items number is {1} its price {2}"
print(my_order.format(quantity,item_no,price))

######################
###the escape charaacter(\...\) allows you to use double quotes 
text="this is fun fair and i has got big \"round ring\""

############################
##Opeartor Precedence

print(3*3+3/3-3)
'''Rules for Mathematical opaerations PEMDAS
P:Paranthesis
E:Exponential
M:Multiplication
D:Division
A:Addtion
S:Substraction
'''
################
################
######LIST######

#we can changes the vaules of list i,e mutable

#irentify the operators
lst=['cherry','banana', 'apple']
print(lst[0])
print(lst[1])

#################################
##Append Method
#add element
lst=['cherry','banana', 'apple']
lst.append("Mango")
print(lst)

##remove the all elements from the list
##clear method
lst=['cherry','banana', 'apple']
lst.clear()
print(lst)

##############################
##copy method
##copy one list into another
lst=['cherry','banana', 'apple']
lst2=lst.copy()
print(lst2)

######################
##count method
##repited element is allowed and returns no of elements

lst=['cherry','banana', 'apple','cherry']
lst.count("cherry")

#################
##extend method
##add two lists
lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
print(lst1)

#######################
##insert method
##insert element in a particular location/index
lst=['cherry','banana', 'apple','cherry']
lst.insert(1, "Mango") #mango is placed at 1st index
print(lst)

###########################3
##pop method
##remove the element
lst=['cherry','banana', 'apple','cherry']
lst.pop(2)  #removing the 2nd index element
print(lst)

#######################
##remove method
##remove the element using element value
lst=['cherry','banana', 'apple','cherry']
lst.remove("cherry")  ##remove only the ONE element of list having same value
print(lst)

################
##reverse method
##reverse the list
lst=['cherry','banana', 'apple','cherry']
lst.reverse()
print(lst)

###########################
##sort method
##
lst=['cherry','banana', 'apple','cherry']
lst.sort()
print(lst)

##################
##################
####TUPLES########

tup=('cherry','banana','apple','cherry')
print(tup)
print(tup[2])

##onces the tuple is created we cannot change the entities i,e imutable
#to change tuple we have to convert tuple into list and futher convert list into tuple 

x=('cherry','banana','apple','cherry')
y="kiwi"
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

########################
#tuples allows to different datatypes
tup=('cherry','banana','apple',345,'cherry')
print(tup)


#################################
#to jion 2 tuples we use + operator

tup1=("a","b","c")
tup2=("d","e","f")
tup3=tup1+tup2
print(tup3)

###################
#####DICTIONARY#####
##key and value pair

dict1={"Brand":"Maruti", "Model":1234, "Year":2012}
print(dict1)
print(len(dict1))


#################################

dict={
      "Brand":["Maruti","Mahindra","Toyota"],
      "Model":["a","b","c"],
      "Year":[2010,2011,2012]
      }
print(dict)

dict.get("Year")
dict.keys()

###############################

car = {
       "brand": ["ford"],
       "model":["mustang"],
       "year":[1965]
       }

x = car.keys()
print(x)
car["color"]="white"
car
x = car.keys()
print(x)

#######################
##removing the element from the dictionary
##pop method in dictionary

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car.pop("model")
print(car)

#############################
##Accessing keys and values in a dictionary
##for loop is required

car = {
       "brand": ["ford"],
       "model":["mustang"],
       "year":[1965]
       }

for x in car:
    print(x) ##accessing keys
    
for x in car: 
    print(car[x])  ##accesing values
    
    
#####################################
##accesing keys and values at a time

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }
for key,value in car .items():
    print("%s == %s" % (key,value))

######################################
##copying dictionary
car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car2 = car.copy()
print(car2)

###Another way:\\
 ''' 
thisdict = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
    }

dict1 = dict(thisdict) 
print(dict1) 
'''

###########################################

our_family = {

    "child1":{
        "name":"Ram",
        "dob":"21-05-2012"
    },

    "child2":{
    "name":"Sham",
    "dob":"21-03-2010"
    }
 
  }

print(our_family)

#######################################
##to remove all elements from the dictionary 
##clear method 

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car.clear()
car     #same as    print(car)

####################################
##creat dictionary with 3 keys assigning the values to all keys 
##fromkey() method


x = {"key1","key2","key3"}
y = "akash"
thisdict = dict.fromkeys(x,y)
thisdict

########################################
##to get the values of the dictionary
#get() method

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car.get("model")

#########################################
#items() returns the dictionary's key-values

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car.items()

###################################
##to display all the values of the dictionary
##values() method

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }

car.values()

########################################
##insert item in the dictionary
##update() method

car = {
       "brand": ["ford"],
       "model":["mustang","sport"],
       "year":[1965]
       }
car.update({"color":"white"})

print(car)

####################################


fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    
    
##use of break
    
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i == "banana"):
        break
    
## 
    
fruits=["apple","banana","orange"]
for i in fruits:
 if(i == "banana"):
    break
 print(i)
 
 
##use of continue 
##skips banana and continue print all elemenets 

fruits=["apple","banana","orange"]
for x in fruits:
    if x == "banana":
     continue
print(x)

################################3
#########range##########
for x in range(2,21):
    print(x)
#########
for x in range(2,21,2):
    print(x)

#######################
##nested loop 

colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
   for y in fruits:
      print(x,y)

#################
##functions
##without argument

def my_function():
    print("Hello from function")
my_function()  #function calling


##with argument

def my_function(name):
 print("Hello"+name) 
my_function("Ram")

############################
##when in function 2 or more than 2 argument are paased they called as position argument 

def my_function(name1,name2):
    print(name1+" "+name2)
my_function("World", "Hello")

#############################
##Arbitrary Argument
'''if we dont know how many arguments that will be
 passed into your function, add * before your parameter
 name 
 '''
 
 def my_function(*kids):
     print(kids[0]+" "+kids[2])
     
 my_function("Hello","Worlds","India")

########################################
##keyword  \\kwargs
##prints keys and values

def my_function(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        
my_function(first="papalal",mid="Mohnlal", last="Goyal")

####################################
##default value function

def my_function(country = "Norway"):
 print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()      #default take Norway as a values
my_function("Brazil")

########################################
##Passing list as argument in function

fruits = ["apple","banana","orange","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)

########################################
##Return Values

def my_function(x):
 return x*5
my_function(5)

##############################
##passed  function 

def my_function1():
    pass         ##pass function without function body defination
    
    
##########################
##Factorial of a number 

def factorial(x):
   if x == 1:
       return 1
   else:
       return(x*factorial(x-1))
   
factorial(3)
factorial(6)

#####################################
####Lambda/Anonymous Function
##lambda function takes any no of arguments
##but only one expression

def add(a):
    sum = a+10
    return sum

add(20)

##########

add  = lambda a:a+10
print(add(20))

################################ 

add = lambda a,b:a+b
print(add(5,6))

###############################
##finding odd numbers from the list
##filter() method accepts 2 arguments

lst = [41,42,43,44,45,46,47,48,49]
odd_lst = list(filter(lambda x:(x%2 != 0),lst))
print(odd_lst)

##finding even numbers from the list

lst = [41,42,43,44,45,46,47,48,49]
even_lst = list(filter(lambda x:(x%2 == 0),lst))
print(even_lst)

########################################
##using lambda function
'''
lst = [11,12,13,14,15]
squ = list(map(lambda x:(x**2),lst))
print(squ)
'''
#########################################


print("Welocome to the roller coaster")
height = int(input("enter your height in cm :"))
if height >= 150:
    print("you are eligible for roller coaster ")
    
    age = int(input("enter your age in years :"))
    bill = 0
    
    if age<12:
        print("child's ticket is 5$")
        bill = 5
        
    elif age>12 and age<18:
      print("your ticket is 10$")
      bill = 10
      
    elif age>18 and age<50:
     print("your ticket is 15$")
     bill = 15
     
    want_photo = input("you want to want photo Y or N : ")
    if want_photo == "Y":
         bill+=3
         print(f"you need to pay {bill} in $ ")
    else:
        print(f"you need to pay {bill} in $ ")
        
else:
    print("you not eligible for roller coaster") 
 
################################################
##BMI CALCULATOR

height = float(input("enter your height in m : "))
weight = float(input("enter your weight in kg : "))
BMI = round((weight/(height*height)),2) 

if BMI<18.5:
    print(f"you are under weight your BMI is :{BMI}")
elif BMI<25 and BMI<18.5:
    print(f"your weight is normal your BMI is:{BMI}")
elif BMI<30 and BMI<35:
    print(f"your obese your BMI is:{BMI}")
elif BMI<30 and BMI<25:
    print(f"your over weight your BMI is:{BMI}")
elif BMI>35:
    print(f"your clinicaly obeseyour BMI is:{BMI}")
       
##########################################
###write a program finding duplicates elements from the list    
##if duplicate print True and if not print false


lst1 = [21,1,6,7,8,9,11,11] 
lst2 = sorted(lst1) 
def is_duplicate(lst2):
    for i in range(len(lst2)-1):
        #comparing current number with next number 
        
        if(lst2[i] == lst2[i+1]):
         return True
    return False
print(is_duplicate(lst2))
   
##################################
### leap year
'''
def leap_year(year):
    if((year > 0) and (year % 100 != 0) and (year % 400 == 0)):
        return True
    return False
print(leap_year(2024))
   ''' 
##############################  
##I.Q
###Pyramid
'''
for i in range(4):
    for j in range(4):
        print("*",end = " ")
    print()
    
    for i in range(4):
        for j in range(i+1):
            print("*",end = " ")
        print()
        
        for i in range(4):
           for j in range(4-i):
              print("*",end = " ")
           print()
  '''

##################H.M:diamond  

########################################
###minimun and maximum from the list

lst = [23,45,2,1,5,7,8,12]
def min_max(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    print("the minimum vaule ", min)
    
    
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    print("the maximun vaule ", max)       
    
min_max(lst)

################################
##palindrom

def is_palindrome(input):
    if input == "":
        return "you entered wrong input"
    else: 
        string = input[::-1]
        if string == input:
         return True
    return False

print(is_palindrome("step on no pets"))

'''same ques above 
a = str(input("enter the string : "))
if input
print(a)
b = str(reversed(a)) 
print(b)
'''
######################################
###

users = ["admin","boss","employee","HR","manager"]
for user in users:
   if user == "admin":
      print("hello",user)
   elif user == "boss":
     print("hello",user)
   elif user == "employee":
      print("hello",user)
   elif user == "HR":
      print("hello",user)
   elif user == "manager":
      print("hello",user)
   else:
       print("hello")
       
########################################
###input from user 

users = ["admin","boss","employee","HR","manager"]
print(users)
user = input("enter the ")
if user == "admin":
      print("hello",user)
elif user == "boss":
     print("hello",user)
elif user == "employee":
      print("hello",user)
elif user == "HR":
      print("hello",user)
elif user == "manager":
      print("hello",user)
else:
       print("hello")

####################################3
####generating random password

import string
adjectives = ['sleepy','slow','smell','wet','brave']
nouns = ['apple','dinosaur','ball','panda','dragon']
#pick the words
import random
adjective = random.choice(adjectives)
noun = random.choice(nouns)
#select a number
number = random.randrange(0, 100)
#select the special character
special_char = random.choice(string.punctuation)
#creat the new secure password
password = adjective + noun + str(number)+ special_char
print("your password is :",password)


#################################################
##using while loop 
import string

adjectives = ['sleepy','slow','smell','wet','brave']
nouns = ['apple','dinosaur','ball','panda','dragon']
import random
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number)+ special_char
    print("your password is :",password)
    response = input("Would you like generated another password ?,enter y or n")
    if response == "n":
        break
    
#########################################  


#######LIST COMREHENSION #######
##I.Q

lst = []
for num in range(0, 20):
    lst.append(num)
print(lst)

######################################
##we can write same method using list comrehesion
lst = [num for num in range(0, 20)]
print(lst)

###########################
##capitalize()
    
names = ['dada', 'mama', 'kaka']
lst = [name.capitalize() for name in names]
print(lst)

###list comrehension using if statement

def is_even(num):
    return num % 2 == 0
lst = [num for num in range(10) if is_even(num)]
print(lst)

##############################
##neasted for loop using list comrehension

lst = [f'{x}{y}'for x in range(3) for y in range(3)]
print(lst)

################################
##Dictionaty comrehension

dict = {x:x*x for x in range(3)}
print(dict)

#################################
######GENERATOR############

##it is another way to creating iterators
#in simple way where it uses keyword 'yield'
##instead of returning it in a defined function
##Generators are implemented using function 

gen = (x for x in range(4))
print(gen)

for num in gen:
    print(num)
    
#####################
##next keyword

gen = (x for x in range(4))
next(gen) ##next keyword gives only one value
next(gen)

###############################
##functions which returns multiple values

def range_even(end):
    for num in range(0,end,2):
       yield num
       
for num in range_even(6):
    print(num)


#####################################
##instead of using for loop we can write our own

def range_even(end):
    for num in range(0,end,2):
       yield num
       
gen = range_even(6)
next(gen)
next(gen)

################################
##Chaining Generators:
    
def lenghts(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
'''
->'ele' appears to be a placeholder for an element
form an iterable The asterisk(*) is liklely
just a chacacter used to represent a placeholder
or a wildcard.
->For a instance, if you're iterating  
over a list of elements, "ele*"
->could symbolize any element in that list 
it's generic representation
->that doesn't correspon to any specific syntax
in python or itertools
'''

passwords = ["not-good", "give'm-pass", "00000010221"]
for password in hide(lenghts(passwords)):
    print(password)

#####################################

import string

nouns = [input("enter the noun: ")]
adjectives = input("enter the adjective: ")

import random
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number)+ special_char
    print("your password is :",password)
    response = input("Would you like generated another password ?,enter y or n")
    if response == "n":
        break
    
def lenghts(password):
    for ele in password:
        yield len(ele)
def hide(password):
    for ele in password:
        yield ele*'*'

password = [password]
for password in hide(lenghts(password)):
    print(password)

####################################
##enumurate 
#printing list with index

lst =["milk","egg","bread"]
for i in range(len(lst)):
    print(f"{i+1} {lst[i]}")
    
    
##by using enumurate
lst =["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
# use of zip function 

name=["dada",'kaka','mama']
info=[12333,13343,87654]
for nm,inf in zip(name,info):
    print(nm,inf)
    
    
#zip function with mismatch list
from itertools import zip_longest
name=["dada",'kaka','mama',"baba"]
info=[12333,13343,87654]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
    
from itertools import zip_longest
name=["dada",'kaka','mama',"baba"]
info=[12333,13343,87654]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
    
###use of all(), if all values are true then it will produce output

lst=[2,3,45,0,65]
if all(lst):
    print("all values are true")
else:
    print("there are  zero true")
    
    
### use of any() 

lst=[0,0,0,0,1]
if any(lst):
    print("it has some values")
else:
    print("all values are  zero ")
    

##count()

from itertools import count
counter= count()
print(next(counter))
print(next(counter))
print(next(counter))


##starting count from where you want
from itertools import count
counter= count(start=10)
print(next(counter))
print(next(counter))
print(next(counter))

###cycle
import itertools

instructions=('eat','code','sleep')
for instruction in itertools.cycle(instructions):
    print(instruction)

#######repeat()
from itertools import repeat
for msg in repeat ('keep patience',times=3):
    print(msg)
    
    
####combinations
from itertools import combinations
player=['john','jani','janardhan']
for i in combinations(player, 2):
    print(i)
    
    
    
from itertools import combinations
player=['john','jani','janardhan',"abhi",'vivek','yashuu']
for i in combinations(player, 3):
    print(i)
    
  
##permutation
from itertools import permutations
player=['john','jani','janardhan']
for i in permutations(player, 2):
    print(i)


from itertools import permutations
player=['0','1']
for i in permutations(player, 2):
    print(i)
    
    
###product()

from itertools import product
team_1=["Rohit","Pandya","Bumrah"]
team_2=["MS","Rahane","Jaddu"]
for pair in product(team_1,team_2):
    print(pair)
    
    '''('Rohit', 'MS')
    ('Rohit', 'Rahane')
    ('Rohit', 'Jaddu')
    ('Pandya', 'MS')
    ('Pandya', 'Rahane')
    ('Pandya', 'Jaddu')
    ('Bumrah', 'MS')
    ('Bumrah', 'Rahane')
    ('Bumrah', 'Jaddu')
    '''
#####################################
##shallow copy and deep copy

list_1=[1,2,3,4,5,6,7,8]
list_2= list_1
list_1[0]=-10
print(list_1)
print(list_2)

#when we want orignal value as it is but want new 
#copy of that then we use shallow copy and deep copy

#Shallow copy
#I.Q

import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

#not affects the other list for level-1 only

list_b[0] = -10
print(list_a)  #[1,2,3,4,5]
print(list_b)  #[-10,2,3,4,5]

#but with nested object
#modifying on level-2 or deep-2

#affects the other list for level-2 if changes list

import copy 
list_a = [[1,2,3,4,5], [6,7,8,9,10]] 
list_b = copy.copy(list_a)
list_b[0][0] = -10
print(list_a)  #[[-10,2,3,4,5], [6,7,8,9,10]]                        
print(list_b)  #[[-10,2,3,4,5], [6,7,8,9,10]]

####DEEP COPY####

##it is used for deep-2 or level-2 or more levels list 
##full independent clones use copy.deepcopy() 
##not affects the other list

import copy 
list_a = [[1,2,3,4,5], [6,7,8,9,10]] 
list_b = copy.deepcopy(list_a)
list_b[0][0] = -10
print(list_a)
print(list_b)

#result:->
#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[1,2,3,4,5],[6,7,8,9,10]]

###################################
#Shallow copy
#I.Q

import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

#not affects the other list for level-1 only

list_b[0] = -10
print(list_a)  #[1,2,3,4,5]
print(list_b)  #[-10,2,3,4,5]

#but with nested object
#modifying on level-2 or deep-2

#affects the other list for level-2 if changes list

import copy 
list_a = [[1,2,3,4,5], [6,7,8,9,10]] 
list_b = copy.copy(list_a)
list_b[0][0] = -10
print(list_a)  #[[-10,2,3,4,5], [6,7,8,9,10]]                        
print(list_b)  #[[-10,2,3,4,5], [6,7,8,9,10]]

####DEEP COPY####

##it is used for deep-2 or level-2 or more levels list 
##full independent clones use copy.deepcopy() 
##not affects the other list

import copy 
list_a = [[1,2,3,4,5], [6,7,8,9,10]] 
list_b = copy.deepcopy(list_a)
list_b[0][0] = -10
print(list_a)
print(list_b)

#[[-10,2,3,4,5],[6,7,8,9,10]]
#[[1,2,3,4,5],[6,7,8,9,10]]


##########################################
##Reading Files

import pandas as pd
f1 = pd.read_csv("c:/1-python/buzzers.csv")
print(f1)

########################

