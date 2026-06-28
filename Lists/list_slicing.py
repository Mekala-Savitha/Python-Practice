# List Slicing

# Definition
# List slicing is used to access a part of a list by specifying
# the start index, stop index, and step value.

# Syntax
# list_name[start : stop : step]

numbers l=[10,20,30,40,50]

# Basic Slicing
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]

# Reverse Using Slicing
print(numbers[::-1])  # [50, 40, 30, 20, 10]

# Different Slicing Examples
print(numbers[::2])   # [10, 30, 50]
print(numbers[1::2])  # [20, 40]
print(numbers[1:5:2]) # [20, 40]
print(numbers[-4:-1]) # [20, 30, 40]
