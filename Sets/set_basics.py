"""
PYTHON SETS - BASICS

Definition:
A set is a built-in Python data type used to store
multiple unique elements. Sets are unordered,
mutable, and do not allow duplicate values.

Syntax:

set_name = {value1, value2, value3}

Empty Set:
set_name = set()
"""

# Example 1: Creating a Set
fruits = {"Apple", "Banana", "Mango"}
print(fruits)

# Example 2: Set with Integers
numbers = {10, 20, 30, 40}
print(numbers)

# Example 3: Set with Different Data Types
data = {10, 3.14, "Python", True}
print(data)

# Example 4: Duplicate Values
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# Example 5: Empty Set
empty = set()
print(empty)

# Example 6: Type of a Set
fruits = {"Apple", "Banana"}
print(type(fruits))

# Example 7: Length of a Set
numbers = {10, 20, 30, 40}
print(len(numbers))

# Example 8: Membership Operator (in)
numbers = {10, 20, 30}
print(20 in numbers)

# Example 9: Membership Operator (not in)
numbers = {10, 20, 30}
print(50 not in numbers)

# Example 10: Traversing a Set
colors = {"Red", "Green", "Blue"}
for color in colors:
    print(color)
