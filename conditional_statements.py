# if statement 
age=10
if age<18:
  print("You are minor")

# if-else statement 
age=23
if age<18:
  print("You are minor")
else:
  print("You are major")

# if-elif-else statement 
age=12
if age<18:
  print("You are minor")
elif(age>18) and (age<60):
  print("You are major")
else:
  print("You are sr.citizen")

# Nested-if statement 
rating=9
if rating>5:
  if(rating>5) and (rating<8):
    print("Good")
  else:
    print("Excellent")
else:
  print("Bad")
  
# Match-case statement 
x=2
match x:
	case 1:
		print("Executing case 1")
	case 2:
		print("Executing case 2")
	case 3:
		print("Executing case 3")

