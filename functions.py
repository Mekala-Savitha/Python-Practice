"""
FUNCTIONS IN PYTHON
Definition :
Function is a block of reusable code that is used to perform some operations.
Functions help reduce code repetition and make programs easier to manage.
"""
"""
User-defined functions 
Definition:
Functions which are created/developed by the programmers are called as user-defined functions.

Syntax:
def function_name(parameters/arguments):
      statements
"""

def greet():
  print("Hello World")
greet()

# Function without parameters 
def xyz():
  print("I am learning python functions")
xyz()

# Function with parameters
def welcome(name):
  print("Good Morning",name)
welcome("Savitha")

def xyz(a):
  a+=23
  print("The updated value of a:",a)
xyz(17)

# Function with multiple parameters 
def qrs(x,y):
  x+=15
  y-=5
  print("The updated value:",x,y)
qrs(20,35.7)

# Function with return value
def xyz(a,b):
  c=a+b
  return c
d=xyz(12,28)
print("The updated value of d:",d)

def abc(x,y):
  c=x+y
  d=x-y
e,f=abc(30,15)
print("The addition value of c:",e)
print("The subtraction value of d:",f)

# Function without return value 
def add(a,b):
  print(a+b)
add(8,7)

# Largest number
def largest(x,y):
      if x>y:
            print(x,"is largest")
      else:
            print(y,"is largest")
largest(35,23)

# Even or Odd
def even_odd(n):
      if n%2==0:
            print("Even")
      else:
            print("Odd")
even_odd(9)

# Factorial 
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)
factorial(6)

# Prime number or not
def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")
prime(7)

# Square of a munber
def square(n):
      return n*n
result=square(7)
print("Square=", result)


