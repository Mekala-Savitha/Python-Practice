"""
PYTHON SET COMPREHENSION

Definition:
Set comprehension is a concise way to create a new set by
iterating over an iterable and optionally applying a condition.

Syntax:

set_name = {expression for item in iterable}

OR

set_name = {expression for item in iterable if condition}
"""


# Example 1: Create a Set of Numbers
numbers = {x for x in range(1, 6)}
print(numbers)


# Example 2: Square of Numbers
squares = {x ** 2 for x in range(1, 6)}
print(squares)


# Example 3: Cube of Numbers
cubes = {x ** 3 for x in range(1, 6)}
print(cubes)


# Example 4: Even Numbers
even = {x for x in range(1, 11) if x % 2 == 0}
print(even)


# Example 5: Odd Numbers
odd = {x for x in range(1, 11) if x % 2 != 0}
print(odd)


# Example 6: Multiples of 5
multiples = {x for x in range(1, 31) if x % 5 == 0}
print(multiples)


# Example 7: Length of Words
words = ["Python", "Java", "HTML", "CSS"]
lengths = {len(word) for word in words}
print(lengths)


# Example 8: First Letter of Each Word
names = ["Savitha", "Anu", "Ravi", "Kiran"]
first_letters = {name[0] for name in names}
print(first_letters)


# Example 9: Convert to Uppercase
languages = {"python", "java", "c"}
uppercase = {lang.upper() for lang in languages}
print(uppercase)


# Example 10: Remove Duplicate Characters
text = "programming"
unique_characters = {ch for ch in text}
print(unique_characters)
