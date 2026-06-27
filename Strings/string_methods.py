"""
String Methods
This program demonstrates commonly used Python string methods for modifying, searching, validating, and formatting strings. It helps understand how to manipulate text efficiently using built-in string functions.
"""

name="python"
print(name.upper())

name="SAVITHA"
print(name.lower())

text="python programming language"
print(text.title())

text="python PROGRAMMING"
print(text.capitalize())

text="  Nivrithi  " 
print(text.strip())

text="  Rithanya  "
print(text.lstrip())

text="  Radhika  "
print(text.rstrip())

sentence="I like Java"
print(sentence.replace("Java","Python"))

text="Banana"
print(text.count("a"))

text="python"
print(text.find("h"))


word="python"
print(word.index("n"))

word="Savitha"
print(word.startswith("Sa"))

text="Savitha"
print(text.endswith("tha"))

text=("Python Java C")
print(text.split())

text=["Python","Java","C"]
print("-".join(text))

text="Savitha"
print(len(text))

word="Python.py"
print(word.removesuffix(".py"))

text="Ms. Savitha"
print(text.removeprefix("Ms. "))

text="Python"
print(text.isalpha())

numbers="73682"
print(numbers.isdigit())

word="Savitha2019"
print(word.isalnum())

text="  "
print(text.isspace())

word="PyThOn"
print(word.swapcase())

text="Python"
print(text.center(8))

text="19"
print(text.zfill(6))
