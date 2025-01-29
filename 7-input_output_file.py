##syntax:
##f = open(file path, mode)

# open the entire file
f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "r")  ##  'r' ---> read mode

##read the file
data = f.read()
print(data)
print(type(data))

##to read the specific park of the file
data = f.read(4)  ##reads only first 4 characters of the file
print(data)
print(type(data))

##if we read() whole file once then readline() prints empty space/line

line1 = f.readline()  ##readas the line of the file
print(line1)  ##reads line 1

line2 = f.readline()  ##readas the line of the file
print(line2)  ##reads line 2

##like this we can read the lines of the file till the end of lines of the file
##after that also we if we're trying to print the readline() then it is printing the enpty line

###############################################################################################

##The file Object Attributes:
'''
1.file.closed
Returns true if file is closed, false otherwise.

2.file.mode
Returns access mode with which file was opened.

3.file.name
Returns name of the file.

4.file.softspace
Returns false if space explicitly required with print, true otherwise.
'''

# Open a file
f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "wb")
print("Name of the file: ", f.name)
print("Closed or not : ", f.closed)
print("Opening mode : ", f.mode)

###############################################################################################
# Check current position

f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "r+")
position = f.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = f.seek(0, 0)

##read the file
print(f.read())

##############################################################################################
# write in the file (w)
'''
w Opens a file for writing only. Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.
'''

f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "w")  ##'w' overwrite the file
##means delete the previous all content and put new content in the file
data1 = f.write("My Name is Akash.")
print(data1)
###########################################################
##Add in the file (a)
'''
a Opens a file for appending. The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode.
If the file does not exist, it creates a new file for writing.'''

f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "a")  ##Add in file, existing content not affected
data = f.write("\nThis is new line")
print(data)
##when we use mode as "w" or "a" if the file is not exists then file is created automatically
################################################################
'''
r+ Opens a file for both reading and writing. The file pointer placed at the beginning of the file.'''

f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "r+")
f.write("Sanjivani COE, Kopargaon this is overwritten content in the file.")  ###overwrite the content from beginning
print(f.read())

###################################################
'''
w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.
# '''
f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "w+")
print(f.read())  ##here nothing is printing because all content is overwritten
f.write("My name is Akash")  ## "My name is Akash" written/appended in the file

#############################################3
'''
a+ Opens a file for both appending and reading. 
The file pointer is at the end of the file if the file exists. The file opens in the append mode.
If the file does not exist, it creates a new file for reading and writing.
'''
f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "a+")
f.write("\nMy sirname is Dhokchaule")
print(f.read())

#######################################
'''
rb Opens a file for reading only in binary format. 
The file pointer is placed at the beginning of the file.
This is the default mode.
'''
f = open("C:\PYTHON\DSA_Python\Topics_of_python.txt", "rb")
print(f.read())

######################################################

##Renaming and Deleting Files
##The rename() Method

import os

f = open(r"C:\PYTHON\DSA_Python\Topics_of_python.txt", "rb")
os.rename(r"C:\PYTHON\DSA_Python\Topics_of_python.txt", r"C:\PYTHON\DSA_Python\1-Topics_of_python.txt")
print("Name of the file: ", f.name)

#################################################
##The remove() Method
f1 = open("C:\PYTHON\BASICS_of_PYTHON\Sample_file_for_removing.docx", "rb")
os.remove("C:\PYTHON\BASICS_of_PYTHON\Sample_file_for_removing.docx")
f1.close()

###############
f.close()##used for closing the file

####################################################
'''
r Opens a file for reading only. 
The file pointer is placed at the beginning of the file. This is the default mode.

rb Opens a file for reading only in binary format. 
The file pointer is placed at the beginning of the file. This is the default mode.

r+ Opens a file for both reading and writing. 
The file pointer placed at the beginning of the file.

rb+ Opens a file for both reading and writing in binary format.
 The file pointer placed at the beginning of the file.

w Opens a file for writing only. Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.

wb Opens a file for writing only in binary format. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.

w+ Opens a file for both writing and reading. 
Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.

wb+ Opens a file for both writing and reading in binary format.
 Overwrites the existing file if the file exists. 
 If the file does not exist, creates a new file for reading and writing.

a Opens a file for appending. 
The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.


ab Opens a file for appending in binary format.
 The file pointer is at the end of the file if the file exists. 
 That is, the file is in the append mode. 
 If the file does not exist, it creates a new file for writing.

a+ Opens a file for both appending and reading.
 The file pointer is at the end of the file if the file exists. 
 The file opens in the append mode. 
 If the file does not exist, it creates a new file for reading and writing.

ab+ Opens a file for both appending and reading in binary format. 
The file pointer is at the end of the file if the file exists.
 The file opens in the append mode. 
 If the file does not exist, it creates a new file for reading and writing.
'''


'''
create a file 'prakash.text' add below data in it
   hi everyone..!
   my name is Akash
   i learn java
   i like java

WAF that replaces all java words with python 
'''

## with function syntax also we can perform all these operations

f2 = open("C:\PYTHON\BASICS_of_PYTHON\prakash.txt", "w+")
data = f2.read()

def write_text():
   f2.write("hi everyone..! \n")
   f2.write("my name is Akash \n")
   f2.write("i learn java \n")
   f2.write(" i like java \n")
write_text()

#read the file
with open(r"C:\PYTHON\BASICS_of_PYTHON\prakash.txt", "r+") as f2:
 new_data = data.replace("java", "python")
 print(new_data)
 data = f2.read()
 print(data)
f2.close()

##################################################################################
##Directories in Python
#Checking if a Directory Exists

import os
directory_path = "C:\PYTHON\BASICS_of_PYTHON"
if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")

#####################################################
##Creating a Directory
import os

# # Create a directory "test"
# os.mkdir("test")
# print ("Directory created successfully")

###################################
##Get Current Working Directory
import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

####################################

