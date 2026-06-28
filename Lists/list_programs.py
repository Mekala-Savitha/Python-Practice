# Print all elements 
names=["savitha","radhika","nivrithi","rithanya"]
print(names)

# Length of a list
print(len(names))

# Print first and last elements of a lis
print("First element=",names[0])
print("Last element=",names[-1])

# Reverse a list using slicing
print("Reverse:",names[::-1])

# Reverse a list using reverse() method
numbers=[11,35,90,22]
numbers.reverse()
print(numbers)

# Largest element
print(max(numbers))

# Smallest element
print(min(numbers))

# Sum of all elements 
print(sum(numbers))

# Average of all elements 
average=sum(numbers)/len(numbers)
print("Average=", average)

# Count even and odd numbers in a list
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even Numbers:",even)
print("Odd Numbers:",odd)

# Count positive and negative numbers in a list
num=[10,-5,0,8,-3,7]
positive=0
negative=0
for n in num:
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
print("Positive Numbers:",positive)
print("Negative Numbers:",negative)

# Search for an element in a list
search=int(input("Enter an element to search:"))
if search in numbers:
        print("Element found")
else:
        print("Element not found")
        
# Count the frequency of a given number
n=[11,90,56,22,11]
print (n.count(11))

# Remove duplicate elements in a list
duplicate=[]
unique=[]

for num in n:
    if num not in unique :
        unique.append(num)
    elif num not in duplicate :
        duplicate.append(num)
print("Duplicate elements=", duplicate)

# Second largest element 
numbers.sort()
print("Second largest element=",numbers[-2])

# Second smallest element 
numbers.sort()
print("Second smallest element=",numbers[1])

# Merge two lists 
list1=[9,3]
list2=[1,5]
list1. extend(list2)
print (list1)

# Ascending order 
numbers. sort()
print("Ascending order=", numbers)

# Descending order 
numbers. sort()
print("Descending order=", numbers[::-1])

# List is empty or not
if numbers==[]:
        print("List is empty")
else:
        print("List is not empty")
        
# Copy a list
new_list=numbers. copy()
print(new_list)

# Remove all occurrences of a specific element 
element=int(input("Enter an element to remove:"))
while element in numbers:
    numbers.remove(element)
print("Updated list=",numbers)

# Index of a element 
print(numbers.index(22))

# Replace an element at a specific index
numbers [1]=45
print(numbers)
