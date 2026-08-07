"""
LAMBDA FUNCTIONS IN PYTHON

Definition:
A lambda function is a small anonymous (nameless) function
that can have any number of arguments but only one expression.
It is mainly used for short and simple operations.

Syntax:
lambda arguments : expression

OR

variable_name = lambda arguments : expression
"""

# Example 1: Lambda Function Without Arguments
greet = lambda: "Hello World"
print(greet())

# Example 2: Square of a Number
square = lambda x: x * x
print(square(5))

# Example 3: Cube of a Number
cube = lambda x: x ** 3
print(cube(3))

# Example 4: Addition of Two Numbers
add = lambda a, b: a + b
print(add(10, 20))

# Example 5: Multiplication of Three Numbers
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))

# Example 6: Find Maximum of Two Numbers
maximum = lambda a, b: a if a > b else b
print(maximum(15, 25))

# Example 7: Find Minimum of Two Numbers
minimum = lambda a, b: a if a < b else b
print(minimum(15, 25))

# Example 8: Check Even or Odd
even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_odd(12))
print(even_odd(15))

# Example 9: Find Length of a String
length = lambda text: len(text)
print(length("Python"))

# Example 10: Convert String to Uppercase
uppercase = lambda text: text.upper()
print(uppercase("python"))
