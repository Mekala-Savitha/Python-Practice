"""
LOOPS IN PYTHON 

Definition:
A loop is used to execute a block of code multiple times or until all items in a sequence are processed.
This reduces code duplication and makes program efficient.

WHILE LOOP
Definition:
A while loop executes as long as the given condition is True.
While loop is used for unknown number of iterations.
"""

# Print 1-50
x=0
while x<51:
  print(x)
  x+=1

# Print 50-1
x=50
while a>=0:
  print(x)
  x-=1

# Content of list
a=[23,89,51,34]
i=0
while i<len(x):
  print(x[i])
  i+=1

# Multiplication of a table
i=1
while i<=10:
  print("3 *",i,"=",3*i)
  i+=1

# First n natural numbers
n=int(input("Enter n:"))
i=1
while i<=n:
  print(i)
  i+=1

# Even numbers
i=2
while i=10:
print(i)
i+=2

# Factorial of a number
n=5
fact=1
while n>0:
  fact*=n
  n-=1
print(fact)

# Sum of natural numbers 
n=5
i=1
s=0
while i<=n:
  s+=i
  i+=1
  print(s)

# Count the digits in a number 
n=58236
count=0
while n>0:
  count+=1
  n//=10
print(count)
