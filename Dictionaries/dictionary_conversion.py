"""
Dictionary Conversion

This file contains programs for converting data between dictionaries and other Python data structures such as lists and tuples. These conversions
are useful for data processing, manipulation, and creating dictionaries
from different sources.

Programs Included

1. Create a dictionary using two lists (zip())
2. Convert a list of tuples to a dictionary
3. Convert a dictionary to a list
4. Convert a list to a dictionary
5. Swap keys and values

Concepts Covered

• Dictionary conversion
• Using zip()
• Using dict()
• Converting lists to dictionaries
• Converting dictionaries to lists
• List of tuples
• Dictionary traversal
• Swapping keys and values

Learning Outcomes

After completing these programs, you will be able to:

• Create dictionaries from two lists using zip().
• Convert a list of tuples into a dictionary.
• Convert dictionaries into lists.
• Convert lists into dictionaries.
• Swap dictionary keys and values.
• Understand different ways to convert data structures in Python.
"""

# Create a dictionary uisng two lists (zip())
list1=["name", "age", "branch"]
list2=["savitha", 22,"CSE"]
student=dict(zip(list1,list2))
print(student)

# Convert a list of tuples to a dictionary 
data_list=[
("name","savitha"),
("age", 22),
("branch","CSE")
]
student=dict(data_list)
print(student)

# Convert a dictionary to a list of key-value  pairs 
student={
    "name":"Savitha",
    "age":22,
    "branch":"CSE"
}
items_list=list(student.items())
print(items_list)

# Convert a list to a dictionary 
keys=["name","age","branch"]
values=["Savitha",22,"CSE"]
student=dict(zip(keys,values))
print(student)
