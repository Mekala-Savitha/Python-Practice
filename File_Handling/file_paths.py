# 
FILE PATHS IN PYTHON
# 


1. WHAT IS A FILE PATH?
# A file path tells Python where a file or folder is located.
# Example:
# data.txt


2. RELATIVE PATH
# A relative path specifies the location of a file
# relative to the current working directory.
# Example:
# data.txt
# files/data.txt


# Example:
with open("data.txt", "r") as file:
    print(file.read())


3. ABSOLUTE PATH
# An absolute path gives the complete location of a file.

# Example:
# /storage/emulated/0/Documents/data.txt

# os.path.abspath() can be used to get the absolute path.

import os
absolute_path = os.path.abspath("data.txt")
print("Absolute Path:", absolute_path)


4. CURRENT WORKING DIRECTORY
# The Current Working Directory (CWD) is the directory
# from which Python is currently working.
# os.getcwd() returns the current working directory.

print("Current Working Directory:")
print(os.getcwd())


5. os.getcwd()
# Definition:
# Returns the current working directory.
# Syntax:
# os.getcwd()
print("Current Working Directory:", os.getcwd())


6. os.path.abspath()
# Definition:
# Returns the absolute path of a file or directory.
# Syntax:
# os.path.abspath(path)
print("Absolute Path:", os.path.abspath("data.txt"))


7. os.path.exists()
# Definition:
# Checks whether a file or directory exists.

# Returns:
# True  -> Path exists
# False -> Path does not exist

# Syntax:
# os.path.exists(path)
print("Exists:", os.path.exists("data.txt"))


8. os.path.isfile()
# Definition:
# Checks whether the given path is a file.

# Returns:
# True  -> Path is a file
# False -> Path is not a file

# Syntax:
# os.path.isfile(path)
print("Is File:", os.path.isfile("data.txt"))


9. os.path.isdir()
# Definition:
# Checks whether the given path is a directory.

# Returns:
# True  -> Path is a directory
# False -> Path is not a directory

# Syntax:
# os.path.isdir(path)
print("Is Directory:", os.path.isdir(".")

      
10. PRACTICAL EXAMPLES

# Example 1:
# Check whether data.txt exists before opening it.
if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist")


# Example 2:
# Check whether data.txt is a file.
if os.path.isfile("data.txt"):
    print("data.txt is a file")
else:
    print("data.txt is not a file")


# Example 3:
# Get the absolute path of data.txt.
path = os.path.abspath("data.txt")
print("File location:", path)


# Example 4:
# Check the current working directory.
current_directory = os.getcwd()
print("Current directory:", current_directory)


# Example 5:
# Check whether the current location is a directory.
if os.path.isdir("."):
    print("Current location is a directory")


11. PRACTICE PROGRAMS

# Practice Program 1:
# Display the current working directory.
print("Current Working Directory:")
print(os.getcwd())


# Practice Program 2:
# Check whether data.txt exists.
print("Exists:", os.path.exists("data.txt"))


# Practice Program 3:
# Check whether data.txt is a file.
print("Is File:", os.path.isfile("data.txt"))


# Practice Program 4:
# Check whether the current location is a directory.
print("Is Directory:", os.path.isdir("."))


# Practice Program 5:
# Display the absolute path of data.txt.
print("Absolute Path:", os.path.abspath("data.txt"))


# Practice Program 6:
# Check whether data.txt exists before reading it.
if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        print(file.read())
else:
    print("data.txt does not exist")


# Practice Program 7:
# Display complete information about data.txt.
print("File:", "data.txt")
print("Exists:", os.path.exists("data.txt"))
print("Is File:", os.path.isfile("data.txt"))
print("Absolute Path:", os.path.abspath("data.txt"))


# Practice Program 8:
# Check whether a path is a file or directory.
path = "data.txt"
if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
else:
    print("Path does not exist")

