"""
CONDITIONAL STATEMENTS IN PYTHON 

Definition:
Conditional Statements allows a program to make decisions based on conditions.
"""

# if statement 
# It allows the program to execute certain code,only when a condition is True.
age=10
if age<18:
  print("You are minor")

# if-else statement 
# The if-else statement is used to choose between two options.
# It executes one block of code if the condition is True and another nlock of code if the condition is False.
age=23
if age<18:
  print("You are minor")
else:
  print("You are major")

# if-elif-else statement 
# This statement is used when you need to check multiple conditions.
age=12
if age<18:
  print("You are minor")
elif(age>18) and (age<60):
  print("You are major")
else:
  print("You are sr.citizen")

# Nested-if statement 
# A nested if statement means an if statement inside another if statement.
rating=9
if rating>5:
  if(rating>5) and (rating<8):
    print("Good")
  else:
    print("Excellent")
else:
  print("Bad")
  
# Match-case statement 
# Match case is a pattern matching statement,used to conpare a value against multiple patterns.
x=2
match x:
	case 1:
		print("Executing case 1")
	case 2:
		print("Executing case 2")
	case 3:
		print("Executing case 3")

