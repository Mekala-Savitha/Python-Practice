"""
Dictionary Sorting

This file contains programs for sorting Python dictionaries based on
their keys and values. Sorting helps organize dictionary data in
ascending or descending order for easier analysis and presentation.

Programs Included

1. Sort Dictionary by Keys
2. Sort Dictionary by Values
3. Sort Dictionary by Keys (Descending)
4. Sort Dictionary by Values (Descending)
5. Sort Dictionary Using sorted()

Concepts Covered

• Dictionary sorting
• Sorting by keys
• Sorting by values
• Ascending order
• Descending order
• sorted() function
• lambda function
• Dictionary traversal

Learning Outcomes

After completing these programs, you will be able to:

• Sort dictionaries by keys in ascending order.
• Sort dictionaries by values in ascending order.
• Sort dictionaries by keys in descending order.
• Sort dictionaries by values in descending order.
• Use the sorted() function with dictionaries.
• Use lambda functions for custom sorting.
"""

# Sort dictionary by keys
student={
    "name":"Savitha",
    "age":22,
    "city":"Hyderabad", 
    "branch":"CSE"
}
for key in sorted(student):
    print(key,  ":" ,student[key])

# Sort dictionary by values
student={
    "name":"Savitha",
    "age":22,
    "city":"Hyderabad", 
    "branch":"CSE"
}
for key,value in sorted(student.items(),key=lambda item: str(item[1])):
    print(key, ":", value) 

# Sort dictionary by keys (Descending)
student={
    "name":"Savitha",
    "age":22,
    "city":"Hyderabad", 
    "branch":"CSE"
}
for key in sorted(student.keys(), reverse=True):
  print(key, ":" , student[key])

# Sort dictionary by values (Descending)
marks = {
    "telugu":81,
    "english":96,
    "maths":90,
    "science":86
}
for key,value in sorted(marks.items(), key=lambda item:item[1],reverse=True):
    print(key, ":", value)

# Sort Dictionary Using sorted()
student={
    "name":"Savitha",
    "age":22,
    "branch":"CSE",
    "city":"Hyderabad"
}
sorted_items=sorted(student.items())
print("Sorted Dictionary Items:")
for key,value in sorted_items:
    print(key, ":", value)
