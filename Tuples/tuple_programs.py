# Tuple Practice Programs

# This section contains beginner-friendly practice programs that apply tuple concepts to solve common programming problems.
# These exercises help improve logical thinking and problem-solving skills by using tuple indexing, slicing, loops, built-in functions, methods, and nested tuples.
# The programs are designed to strengthen your understanding of tuple operations through practical examples.

# Chevk whether an element exists in a tuple
t=(11,27,34,67)
num=int(input("Enter a number:"))
if num in t:
    print("Found")
else:
    print("Not Found")

# Display the first, middle, and last elements of a tuple
num=(1,5,9,3,6)
print("First element:",num[0])
print("Middle element:",num[len(num)//2])
print("Last element:",num[-1])

# Find the average without using sum() and len()
num=(9,3,5,2)
total=0
count=0
for i in num:
    total+=i
    count+=1
average=total/count
print("Average:", average)

# Find the largest and smallest values without using max() and min()
numbers=(25,10,45,5,30,60)
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest value:",largest)
print("Smallest value:",smallest)

# Count even and odd numbers in a tuple
t=(5,8,3,6,1)
even=0
odd=0
for num in t:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("Odd numbers:",odd)

# Create a tuple from user input and print all its elements
numbers=tuple(map(int,input("Enter numbers separated by space:").split()))    
print("Tuple:",numbers)
print("Elements of the Tuple:")
for i in numbers:
    print(i)

# Find the second largest element in a tuple
numbers=(25,10,45,5,30,60)
sorted_numbers=sorted(numbers)
print("Second largest element:", sorted_numbers[-2])

# Find the second smallest element in a tuple
numbers=(25,10,45,5,30,60)
sorted_numbers=sorted(numbers)
print("Second smallest element:", sorted_numbers[1])

# Count positive and negative numbers in a tuple
numbers=(10,-5,20,-8,0,15,-3)
positive=0
negative=0
for i in numbers:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
print("Positive numbers:",positive)
print("Negative numbers:",negative)

# Find Duplicate Elements in a Tuple
numbers=(1, 2, 3, 2, 4, 5, 1, 6)
duplicates=[]
for i in numbers:
    if numbers.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate elements:", tuple(duplicates))

# Remove Duplicate Elements from a Tuple
numbers=(1,2,3,2,4,5,1,6)
unique=tuple(set(numbers))
print("Tuple after removing duplicates:",unique)

# Merge Two Tuples
tuple1=(10,20,30)
tuple2=(40,50,60)
merged=tuple1+tuple2
print("Merged tuple:",merged)

# Check Whether Two Tuples Are Equal
tuple1=(10,20,30)
tuple2=(10,20,30)
if tuple1==tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")

# Find the Frequency of Each Element in a Tuple
numbers=(1,2,3,2,4,1,5,2)
printed=()
for i in numbers:
    if i not in printed:
        print(i, ":", numbers.count(i))
        printed += (i,)

# Nested tuple
t=((1,5),(7,3))
print("Nested Tuple:",t)
print("First inner tuple:",t[0])
print("Second inner tuple:",t[1])

print("First element of first tuple:",t[0][0])
print("Second element of first tuple:",t[0][1])

print("First element of second tuple:",t[1][0])
print("Second element of second tuple:",t[1][1])
