"""
Dictionary Operations

This file contains programs that perform various operations on Python
dictionaries. These operations help in searching, comparing, sorting,
and performing calculations on dictionary data.

Programs Included

1. Find the key with the maximum value
2. Find the key with the minimum value
3. Find the maximum key
4. Find the minimum key
5. Sum of all dictionary values
6. Multiply all dictionary values
7. Average of all dictionary values
8. Swap keys and values
9. Find common keys
10. Dictionary equality

Concepts Covered

• Dictionary traversal
• Maximum and minimum operations
• Mathematical operations on dictionary values
• Swapping keys and values
• Comparing dictionaries
• Finding common keys
• Dictionary methods
• Loops
• Conditional statements

Learning Outcomes

After completing these programs, you will be able to:

• Find the maximum and minimum keys or values in a dictionary.
• Calculate the sum, product, and average of dictionary values.
• Swap keys and values in a dictionary.
• Find common keys between two dictionaries.
• Compare two dictionaries for equality.
• Apply loops and conditional statements to perform dictionary operations.
"""

# Key with maximum value
marks={"telugu":81,"english":96,"maths":90,"science":86}
max_key=max(marks,key=marks.get)
print("Key with maximum value:",max_key)
print("Maximum value:",marks[max_key])

# Key with minimum value 
marks={"telugu":81,"english":96,"maths":90,"science":86}
min_key=min(marks,key=marks.get)
print("Key with minimum value:",min_key)
print("Minimum value:",marks[min_key])

# Maximum key 
marks={"telugu":81,"english":96,"maths":90,"science":86}
max_key=max(marks.keys())
print("Maximum Key:",max_key)

# Minimum key
marks={"telugu":81,"english":96,"maths":90,"science":86}
min_key=min(marks.keys())
print("Minimum Key:",min_key)

# Sum of all dictionary values
marks={"telugu":81,"english":96,"maths":90,"science":86}
total=0
for value in marks.values():
  total+=value
print("Sum of all dictionary values:", total)

# Product of all dictionary values
marks={"telugu":81,"english":96,"maths":90,"science":86}
product=1
for value in marks.values():
    product*=value
print("Product of all dictionary values:",product)

# Average of all dictionary values
marks={"telugu":81,"english":96,"maths":90,"science":86}
total=0
for value in marks.values():
    total+=value
average=total/len(marks)
print("Average of all dictionary values:",average)

# Swap keys and values
data={"A":123,"B":456,"C":789}
swapped={}
for key,value in data.items():
  swapped[value]=key
print("Original Dictionary:",data)
print("Swapped Dictionary:",swapped)

# Find common keys
data1={"name":"savitha", "age":22,"branch":"CSE"}
data2={"college":"SCTC", "marks":96,"name":"savitha"}
for key in data1. keys():
    if key in data2. keys():
        print(key)     

# Dictionary equality 
dict1={"name":"savitha", "age":22,"branch":"CSE"}
dict2={"age":22,"branch":"CSE","name":"savitha"}
if dict1==dict2:
  print("Dictionaries are equal")
else:
  print("Dictionaries are not equal")
