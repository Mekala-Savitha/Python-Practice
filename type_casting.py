"""
TYPE CASTING IN PYTHON 

Definition:
Type Casting is a process converting the variable values of one datatype into anither datatype.
"""

# Implicit type casting
# In this,the python interpreter automatically converts one datatype values into another datatype without programmer intervention.
x=39
y=64.19
z=x+y
print(z)
print(type(z))

# Explicit type casting 
# In this,the pragrammer manually converts the variables of one datatype into another datatype with the help of built-in functions.
a=25.13
b=45
c=int(a+b)
print(c)
print(type(c))

# List to Set
s=[1,9,8,3]
t=set(s)
print(t)
print(type(t))
