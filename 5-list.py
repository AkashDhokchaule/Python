##Python Lists
##List
'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)

###################################
#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

########Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


##List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:
list4 = ["abc", 34, True, 40, "male"]

##type()

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

##The list() Constructor
##It is also possible to use the list() constructor when creating a new list

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#####################################################
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

1.List 
     is a collection which is ordered and changeable. Allows duplicate members.
2.Tuple 
      is a collection which is ordered and unchangeable. Allows duplicate members.
3.Set 
      is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4.Dictionary 
    is a collection which is ordered** and changeable. No duplicate members.
'''
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#####Python - Access List Items

##List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

##Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

##Range of Indexes
#You can specify a range of indexes by specifying where to 
##start and where to end the range.
#When specifying a range, the return value will be 
#a new list with the specified items.


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
##Return the third, fourth, and fifth item:

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

##Check if Item Exists
#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###############################################################
##Python - Change List Items

##Change Item Value
#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

##Change a Range of Item Values
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

##If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
######################################################
##Python - Add List Items

##Append Items
##To add an item to the end of the list, use the append() method:
#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

########################
##Insert Items
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

###########################################
##Extend List

#To append elements from another list to the current list, use the extend() method.
#Add the elements of tropical to thislist:
##The elements will be added to the end of the list.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#############
##Add Any Iterable

#The extend() method does not have to append lists, 
#you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###################################################
##Python - Remove List Items

#Remove Specified Item

#The remove() method removes the specified item.
#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#########################
##Remove Specified Index
#The pop() method removes the specified index.
#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

##If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

##########################

#The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

######################
#The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist

#############################################
##Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#############################################################
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##########Python - Loop Lists

##Loop Through a List
#You can loop through the list items by using a for loop:

#Get your own Python Server
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

##############
##Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

#Example
#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

##################################
##Using a While Loop
#You can loop through the list items by using a while loop.

#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

#Remember to increase the index by 1 after each iteration.
#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#################################
####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

##Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

####################################################
###Loop Through a List
##You can loop through the list items by using a for loop:

#Example
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
########################################
####Loop Through the Index Numbers
##You can also loop through the list items by referring to their index number.

#Use the "range()" and "len()" functions to create a suitable iterable.

#Example
#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


######################################

####Using a While Loop
##You can loop through the list items by using a while loop.

##Use the "len()" function to determine the length of the list, 
##then start at 0 and loop your way through the list items by 
##referring to their indexes.
#Remember to increase the index by 1 after each iteration.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


##########################################
##Looping Using List Comprehension
##List Comprehension offers the shortest syntax for looping through lists:

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


##################################################
############Python - List Comprehension
#####List Comprehension
##List comprehension offers a shorter syntax when you want to 
##create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, 
##containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a 
##for statement with a conditional test inside:

#Example
#Get your own Python Server

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#########################################
##Condition
#The condition is like a filter that only accepts the items that 
##valuate to True.

#Only accept items that are not "apple":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#The condition if x != "apple"  will return True for all elements other than "apple",
##making the new list contain all fruits except "apple"

############
###The condition is optional and can be omitted:

#With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

###############################
####Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.

#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
print(newlist)

####Same example, but with a condition:

##Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print(newlist)

####################
##Expression
#The expression is the current item in the iteration, 
# #but it is also the outcome, which you can manipulate before 
# #it ends up like a list item in the new list:

#Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#############You can set the outcome to whatever you like:
#Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

##The expression can also contain conditions, 
##not like a filter, but as a way to manipulate the outcome:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


####$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#################################################
#######Python - Sort Lists
####Sort List Alphanumerically
##List objects have a sort() method that will sort the list alphanumerically, 
##ascending, by default:

#Get your own Python Server
#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

##########
##Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

##########################################
##Sort Descending
#To sort descending, use the keyword argument reverse = True:

#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

################################################################3
####Customize Sort Function
##You can also customize your own function by using the keyword 
##argument key = function.

#The function will return a number that will be used to sort the list 
##(the lowest number first):

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


####Case Insensitive Sort
#By default the sort() method is case sensitive, 
#resulting in all capital letters being sorted before lower case letters:

#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

###########################################################################
##Luckily we can use built-in functions as key functions when sorting a list.
##So if you want a case-insensitive sort function, use str.lower as a 
##key function:

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#################################################################3
###Reverse Order
##What if you want to reverse the order of a list, 
##regardless of the alphabet?

##The reverse() method reverses the current sorting order of the elements.

#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


###$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##############################################################

###Python - Copy Lists
##You cannot copy a list simply by typing list2 = list1, because: list2
##will only be a reference to list1, and changes made in list1 will 
##automatically also be made in list2.

##Use the copy() method
#You can use the built-in List method copy() to copy a list.

#Make a copy of a list with the copy() meth

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

################

#Use the list() method
#Another way to make a copy is to use the built-in method list().

#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

################################
##Use the slice Operator
##You can also make a copy of a list by using the : (slice) operator.

#Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

###################################################################
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

###Python - Join Lists

##There are several ways to join, or concatenate, two or more lists in Python.
##One of the easiest ways are by using the + operator.

#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

###############################
##Another way to join two lists is by appending all the items from
##list2 into list1, one by one:

#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

############
##Or you can use the extend() method, where the purpose is
# to add elements from one list to another list:


#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

###########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##############################################################3
####List Methods

##https://www.w3schools.com/python/python_lists_methods.asp