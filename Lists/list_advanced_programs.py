# Find Common Elements in Two Lists
# Definition:
# Common elements are the values that are present in both lists.
list1=[10,20,30,40]
list2=[30,40,50,60]
common=[]
for num in list1:
    if num in list2:
        common.append(num)
print("Common elements=",common)

# Elements Present in the First List but Not in the Second List
# Definition:
# list1 = [10, 20, 30, 40]
# These are the elements that exist in the first list but are not present in the second list.
list1=[10,20,30,40]
list2=[30,40,50,60]
result=[]
for num in list1:
    if num not in list2:
        result.append(num)
print("Elements present in the first list but not in the second list =", result)

# Separate Even and Odd Numbers into Two Different Lists
# Definition:
# Separate all even numbers into one list and all odd numbers into another list.
numbers=[10,15,22,7,8,11]
even=[]
odd=[]
for num in numbers:
    if num % 2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers=",even)
print("Odd numbers=",odd)

# Separate Positive and Negative Numbers into Two Different Lists
# Definition:
# Separate all positive numbers into one list and all negative numbers into another list.
numbers=[10,-5,0,8,-3,7]
positive = []
negative = []
for num in numbers:
    if num>0:
        positive.append(num)
    elif num<0:
        negative.append(num)
print("Positive numbers=",positive)
print("Negative numbers=",negative)

# Maximum and Minimum Values Without Using max() and min()
numbers=[25,10,45,5,30]
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print("Largest element=",largest)
print("Smallest element=",smallest)

# Rotate a List to the Left by One Position
# Definition:
# Rotating a list to the left by one position means moving the first element to the end of the list, while shifting all other elements one position to the left.
numbers=[10,20,30,40,50]
numbers=numbers[1:]+numbers[:1]
print("Left rotated list =",numbers)

# Rotate a List to the Right by One Position
# Definition:
# Rotating a list to the right by one position means moving the last element to the beginning of the list, while shifting all other elements one position to the right.
numbers=[10,20,30,40,50]
numbers=numbers[-1:]+numbers[:-1]
print("Right rotated list =", numbers)

# Remove All Even Numbers from a List
# Definition:
# Remove every even number from the list and keep only the odd numbers.
numbers=[10,15,22,7,8,11]
odd=[]
for num in numbers:
    if num % 2!=0:
        odd.append(num)
print("List after removing even numbers=",odd)

# Remove All Odd Numbers from a List
# Definition:
# Remove every odd number from the list and keep only the even numbers.
numbers=[10,15,22,7,8,11]
even=[]
for num in numbers:
    if num % 2==0:
        even.append(num)
print("List after removing odd numbers =",even)
