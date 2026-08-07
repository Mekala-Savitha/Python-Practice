"""
MAP FUNCTION IN PYTHON

Definition:
The map() function applies a specified function to each item
of an iterable (such as a list, tuple, or set) and returns
a map object.

Syntax:
map(function, iterable)
"""

# Example 1: Square of Numbers
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x*x, numbers)
print(list(result))

# Example 2: Cube of Numbers
numbers = [1, 2, 3, 4]
result = map(lambda x: x**3, numbers)
print(list(result))

# Example 3: Add 10 to Each Number
numbers = [10, 20, 30]
result = map(lambda x: x+10, numbers)
print(list(result))

# Example 4: Convert to Uppercase
names = ["python", "java", "html"]
result = map(lambda x: x.upper(), names)
print(list(result))

# Example 5: Find Length of Strings
words = ["apple", "banana", "kiwi"]
result = map(len, words)
print(list(result))

# Example 6: Convert String Numbers to Integers
numbers = ["10", "20", "30"]
result = map(int, numbers)
print(list(result))

# Example 7: Convert Integers to Strings
numbers = [1, 2, 3]
result = map(str, numbers)
print(list(result))

# Example 8: Multiply by 5
numbers = [2, 4, 6]
result = map(lambda x: x*5, numbers)
print(list(result))

# Example 9: Calculate Squares of Even Numbers
numbers = [2, 4, 6, 8]
result = map(lambda x: x*x, numbers)
print(list(result))

# Example 10: First Letter Capital
names = ["savitha", "anu", "ravi"]
result = map(lambda x: x.capitalize(), names)
print(list(result))
