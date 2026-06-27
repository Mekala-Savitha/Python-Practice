"""
String Indexing
String indexing is used to access individual characters in a string using their position (index). Python supports both positive and negative indexing.
"""

# Access characters using indexing
word="Savitha"
print(word[0])
print(word [2])
print(word[3])
print(word[5])
print(word[-4])
print(word[-1])

# User input indexing
text=input("Enter a String:")
print("First character:",text[0])
print("Last character:",text[-1])

# Printing each character uisng indexing 
name="Savitha"
for i in range(len(name)):
  print(name[i])
