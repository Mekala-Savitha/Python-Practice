# List
a=[7,2,5]
b=[9,6,1]
for c in a:
  for d in b:
    print(c,d)

# ATM Pin
attempts=0
while attempts<3:
  Pin=input("Enter Pin:")
  if Pin=="2019":
    print("Access Granted")
    break
  attempts+=1

# Rectangle Pattern 
rows=3
cols=5
for i in range(rows):
  for j in range(cols):
    print("*",end="")
  print()

# Right Triangle Pattern 
for i in range(1,6):
  for j in range(i):
    print("*",end="")
  print()

# Number Triangle 
for i in range(1,6):
  for j in range(i):
    print(i,end="")
  print()

# Floyd's Triangle 
num=1
for i in range(1,6):
  for j in range(i):
    print(num,end="")
    num+=1
  print()

# Hollow Square
n=5
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j ==0 or j==n-1:
      print("",end="")
  print()
