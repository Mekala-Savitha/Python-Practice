"""
FUNCTION ARGUMENTS IN PYTHON

Definition:
Arguments are values passed to a function when it is called.
They allow a function to work with different data.

Types of Arguments:
1. Positional Arguments:
The number of arguments in the function call should match exactly with the function.
2. Keyword Arguments:
Keywords can also be passed as arguments.
3. Default Arguments:
A default value is assigned to a parameter.
4. Variable-Length Arguments (*args)
5. Keyword Variable-Length Arguments (**kwargs)
"""

# Positional Arguments 
def student(name,age):
  print(name,age)
student("Savitha",22)

# Keyword Arguments 
def abc(int,float):
  print(int,float)
abc(39,60.4)

def student(name,age):
  print(name,age)
student(age=22,name="Savitha")

# Default Arguments 
def greet(name="Guest"):
  print("Hello",name)
greet()
greet("Nivrithi")

# Variable Length Arguments(*args)
def add(*numbers):
  print(sum(numbers))
add(17,25,13)

# Keyword Variable Length Arguments(**Kwargs)
def xyz(**a):
  print(a)
xyz(int=30,float=46.7)

