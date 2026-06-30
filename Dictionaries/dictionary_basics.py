"""
Dictionary Basics

This file contains the basic Python dictionary programs for beginners.
It covers creating dictionaries, accessing values, adding, updating,
deleting elements, and traversing dictionary data.

Programs Included

1. Create a dictionary
2. Access values using keys
3. Add a new key-value pair
4. Update a value
5. Delete a key
6. Print all keys
7. Print all values
8. Print all items
9. Check if a key exists
10. Count the number of key-value pairs

Concepts Covered

• Dictionary creation
• Key-value pairs
• Accessing values
• Adding new items
• Updating existing values
• Deleting items
• Traversing dictionaries
• Membership testing
• Dictionary length

Learning Outcomes

After completing these programs, you will be able to:

• Create Python dictionaries.
• Access dictionary values using keys.
• Insert new key-value pairs.
• Modify existing dictionary values.
• Delete dictionary elements.
• Iterate through keys, values, and items.
• Check whether a key exists.
• Count dictionary elements using len().
"""

# Create a dictionary 
student = {
    "name":"Savitha",
    "age":22,
    "city":"Hyderabad", 
    "branch":"CSE"
}
print(student)

# Access values using keys 
print(student.get("name"))
print(student.get("age"))
print(student.get("city"))
print(student.get("branch"))

# Add a new key-value pair
student["college"]="Sri Chaitanya Technical Campus"
print(student)

# Update a value 
student["age"]=21
print(student)

# Delete a key
del student["branch"]
print(student)

# Print all keys
for key in student.keys():
    print(key)

# Print all values
for value in student. values():
    print(value)

# Print all items
for key, value in student.items():
    print(key, value)

# Check if a key exists 
key=input("Enter a key:")
if key in student:
    print("Found")
else:
    print("Not Found")

# Count the number of key-value pairs
print(len(student))
