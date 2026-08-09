# 
PYTHON FILE HANDLING - BASICS
# 


1. OPENING A FILE
# open() is used to open a file.
# Syntax:
# file = open("filename", "mode")

# Simple Example:
file = open("data.txt", "r")
print(file)
file.close()


2. FILE MODES
# r -> Read
# w -> Write / Overwrite
# a -> Append
# x -> Create a new file


2.1 r - READ MODE
# Opens an existing file for reading.
file = open("data.txt", "r")
print(file.read())
file.close()


2.2 w - WRITE MODE
# Opens a file for writing.
# If the file exists, its previous content is overwritten.
# If the file does not exist, it is created.
file = open("data.txt", "w")
file.write("Hello Python")
file.close()


2.3 a - APPEND MODE
# Adds new content at the end of the existing file.
file = open("data.txt", "a")
file.write("\nWelcome to File Handling")
file.close()


2.4 x - CREATE MODE
# Creates a new file.
# It gives FileExistsError if the file already exists.
file = open("new_file.txt", "x")
file.write("This is a new file.")
file.close()


3. READING A FILE
# ------------------------------------------------------------

3.1 read()
# read() reads the entire content of a file.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# Reading a specific number of characters:
file = open("data.txt", "r")
content = file.read(5)
print(content)
file.close()


3.2 readline()
# readline() reads one line at a time.
file = open("data.txt", "r")
line = file.readline()
print(line)
file.close()


# Reading multiple lines using readline():
file = open("data.txt", "r")
print(file.readline())
print(file.readline())
file.close()


3.3 readlines()
# readlines() reads all lines and returns them as a list.
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# Reading and displaying each line:
file = open("data.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()


4. WRITING TO A FILE
# ------------------------------------------------------------

4.1 write()
# write() writes a string into a file.
file = open("data.txt", "w")
file.write("Python is easy to learn.")
file.close()


# Writing multiple strings:
file = open("data.txt", "w")
file.write("Python\n")
file.write("Java\n")
file.write("SQL\n")
file.close()


4.2 writelines()
# writelines() writes multiple strings into a file.
lines = ["Python\n", "Java\n", "SQL\n"]
file = open("data.txt", "w")
file.writelines(lines)
file.close()


# Writing a list of student names:
students = [
    "Savitha\n",
    "Anjali\n",
    "Priya\n"
]
file = open("data.txt", "w")
file.writelines(students)
file.close()


5. CLOSING A FILE
# close() closes an opened file.
file = open("data.txt", "r")
print(file.read())
file.close()


# Checking whether the file is closed:
file = open("data.txt", "r")
print(file.closed)
file.close()
print(file.closed)


6. with open()
# with open() is the recommended way to work with files.
# It automatically closes the file after the block finishes.
# Syntax:
# with open("filename", "mode") as file:
#     statements


# 6.1 Reading Example
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
  
        
# 6.2 Writing Example
with open("data.txt", "w") as file:
    file.write("Learning Python File Handling")
  
