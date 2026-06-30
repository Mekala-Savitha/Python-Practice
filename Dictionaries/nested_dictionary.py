"""
Nested Dictionary

This file contains programs related to nested dictionaries in Python.
A nested dictionary is a dictionary that contains one or more dictionaries
as its values. It is useful for storing structured and hierarchical data.

Programs Included

1. Create a nested dictionary
2. Access nested dictionary values
3. Update a nested dictionary
4. Delete nested dictionary values

Concepts Covered

• Nested dictionaries
• Accessing nested values
• Updating nested data
• Deleting nested key-value pairs
• Traversing nested dictionaries

Learning Outcomes

After completing these programs, you will be able to:

• Create nested dictionaries.
• Access values inside nested dictionaries.
• Update values in nested dictionaries.
• Add new key-value pairs to nested dictionaries.
• Delete values from nested dictionaries.
• Understand how hierarchical data is represented using dictionaries.
"""

# Create a nested dictionary 
student={
"name":"savitha",
"marks":{
"maths":95,
"science":93,
"english":96
}
}
print(student)

# Access nested dictionary values 
print("\nAccess Nested Values:")
print(student ["marks"]["maths"])
print(student ["marks"]["science"])
print(student ["marks"]["english"])

# Update a nested dictionary 
student ["marks"]["telugu"]=90
print("\nAfter Updating:")
print(student)

# Delete nested dictionary values 
del student ["marks"]["science"]
print("\nAfter Deleting:")
print(student)
