"""
FOR LOOP

Definition:
For loop is used when the number of iterations are known in advance.
"""

# String
name="Savitha"
for letter in name:
  print(letter)

# List elements 
fruits=["Mango","Banana","Apple"]
for fruit in fruits:
  print(fruit)

# Multiplication table 
n=int(input("Enter a number:"))
for i in range(1,11):
  print("2 *",i,"=",2*i)

# Greet person names starts with 'S'
l1=["Savitha","Ravi","Sita","Anu"]
for name in l1:
  if name.startswith("S"):
    print("Hello",name)

# Prime number or not
n=12
if n<=1:
else:
  for i in range(2,n):
    if n%i==0:
      print("Not Prime")
      break
    else:
      print("Prime")

# Factorial 
n=6
fact=1
for i in range(1,n+1):
  fact*=i
  print(fact)

# Star pattern
for i in range(1,6):
  print("*", *i)

# Inverted star pattern
for i in range(5,0,-1):
  print("*",*i)


x=3
for i in range(1,x+1):
  for j in range(x-i):
    print("",end="")
  for k in range(2*i-1):
    print("*",end="")
print()


for i in range(3):
  for j in range(3):
    if i==1 and j==1:
      print("",end="")
    else:
      print("*",end="")
  print()

# Factors of a number
n=6
for i in range(1,n+1):
  if n%i==0:
    print(i)

# Vowels count
s="Savitha"
count=0
for ch in s:
  if ch in "aeiouAEIOU":
    count+=1
print("Number of vowels:",count)

# Reverse a string
s="Chinni"
rev=""
for i in range(len(s)-1,-1,-1):
  rev+=s[i]
print("Reversed string:",rev)

# Fibonacci series 
n=10
a=0
b=1
for i in range(n):
  print(a,end="")
  c=a+b
  a=b
  b=c

# Square pettern
for i in range(4):
  print("****")
