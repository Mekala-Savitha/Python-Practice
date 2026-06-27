"""
String Slicing

String slicing is used to extract a portion of a string by specifying a start and end index. It can also be used to reverse a string.
"""

# Basic slicing
word="PYTHON"
print(word[1:4])
print(word[:4])
print(word[2:])
print(word[:])
print(word[2:5])

# Reverse a string 
text=input("Enter a string:")
print("Reverse:",text[::-1])

# First and Last three characters 
name=input("Enter a name:")
print("First 3 characters:",name[:3])
print("Last 3 characters:",name[-3:])
