# Tuple Packing and Unpacking

# Tuple packing is the process of storing multiple values in a single tuple, while tuple unpacking is the process of assigning tuple elements to individual variables.
# Python also supports extended unpacking using the * operator, which collects multiple elements into a single variable.
# This section demonstrates different ways to pack and unpack tuples, including basic unpacking, extended unpacking, and swapping variables using tuple unpacking.

# Tuple Packing 
student=("Savitha",22,"CSE")
print(student)

# Tuple Unpacking
student=("Savitha",22,"CSE")
name,age,branch=student
print(name)
print(age)
print(branch)

# Packing and Unpacking using *
student=("Savitha",22,"CSE","Python","Java")
name,age,*details=student
print(name)
print(age)
print(details)

# * at the Beginning 
numbers=(9,2,6,1,7)
*start,last=numbers
print("Start:",start)
print("Last:",last)

# * in the Middle
numbers=(9,2,6,1,7)
first,*middle,last=numbers
print("First:",first)
print("Middle:",middle)
print("Last:",last)

# * at the End
numbers=(9,2,6,1,7)
first,*remaining=numbers
print("First:",first)
print("Remaining:",remaining)

# Swap Two Variables Using Tuple Unpacking
a=13
b=27
a,b=b,a
print("a=",a)
print("b=",b)

# Unpack and Print Student Details
student=("Savitha",22,"CSE","Hyderabad")
name,age,branch,city=student
print("Name:",name)
print("Age:",age)
print("Branch:",branch)
print("City:",city)

# Print the Type of * Variable
numbers=(1,2,3,4,5)
first,*remaining=numbers
print(remaining)
print(type(remaining))

# Unpack User Information
user=("Savitha",22,"Python","India")
name,age,course,country=user
print("Name:",name)
print("Age:",age)
print("Course:",course)
print("Country:",country)
