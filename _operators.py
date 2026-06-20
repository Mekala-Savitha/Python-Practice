"""
OPERATORS IN PYTHON 

Definition:
Operators are the symbols which are used to perform specific operation on different variables and their values.
"""

# Arithmetic operators 
# These are used on two operands to perform mathematical operations like addition,subtraction,etc..
x=23
y=17
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("Remainder:",x%y)
print("Power:",x**y)
print("Floor Division:",x//y)

#Comparison operators 
# These are used for comparing two variable values and return a boolean values as either True or False.
a=53
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Logical operators 
# Logical operators are used to make logical decisions of conditions in a program.
s=5
t=10
print(s<10 and t>5)
print(s>10 or t<8)
a=True
print(not a)

# Assignment operators
# We can assign the right side expression's value to the operands variable.
a=10
a+=5
print(a)
a-=5
print(b)
a%=4
print(a)
a**=2
print(a)

# Bitwise operators 
# Bitwise operators works on bits and perfoms bit by bit operation.
x=5
y=2
print(x&y)
print(x|y)
print(x^y)
print(~y)
print(x<<2)
print(y>>1)

# Membership operators 
# These are allow to verify the membership of a value is persent inside a sequence datatype varible or not 
name="Savitha"
print("a" in name)
print("w" in name)
