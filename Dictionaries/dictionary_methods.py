"""
Dictionary Methods

This file contains programs demonstrating the built-in methods of Python
dictionaries. These methods help perform common operations such as
retrieving, updating, copying, deleting, and creating dictionaries.

Programs Included

1. Merge two dictionaries
2. Copy a dictionary
3. Clear a dictionary
4. Create a dictionary using dict()
5. Use get()
6. Use setdefault()
7. Use pop()
8. Use update()
9. Use popitem()
10. Use fromkeys()

Concepts Covered

• Dictionary methods
• Creating dictionaries
• Accessing values safely
• Adding default values
• Updating dictionaries
• Removing key-value pairs
• Copying dictionaries
• Clearing dictionary contents
• Creating dictionaries from keys

Learning Outcomes

After completing these programs, you will be able to:

• Create dictionaries using the dict() constructor.
• Retrieve values using get().
• Add default values using setdefault().
• Update dictionaries using update().
• Remove items using pop() and popitem().
• Copy dictionaries using copy().
• Remove all items using clear().
• Create dictionaries with predefined keys using fromkeys().
• Merge two dictionaries efficiently.
"""

# Merge two dictionaries 
# For different keys
dict1={"name":"Savitha","age":22}
dict2={"city":"Hyderabad","branch":"CSE"}
dict1. update(dict2)
print(dict1)

# For same keys
dict1={"name":"Savitha","age":22}
dict2={"city":"Hyderabad", "age":21}
dict1. update(dict2)
print(dict1)

# Copy a dictionary 
new=student. copy()
print(new)

# Clear a dictionary 
dict1. clear()
print(dict1)

# Create a dictionary using dict()
student=dict(name="savitha", age=22,branch="CSE")
print(student)

# Use get()
print(student. get("branch"))

# Use setdefault()
student.setdefault("marks", 356)
print(student)

# Use pop()
student.pop("age")
print(student)

# Use update()
student. update({"city":"Hyderabad"})
print(student)

# Use popitem()
student.popitem()
print(student)

# Use fromkeys()
keys=["x", "y", "z"]
d=dict.fromkeys(keys,0)
print(d)
