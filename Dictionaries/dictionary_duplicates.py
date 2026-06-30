"""
Dictionary Duplicates

This file contains programs for finding and removing duplicate values in Python dictionaries. These programs help understand how to identify
repeated values and create dictionaries with unique values.

Programs Included

1. Find Duplicate Values
2. Remove Duplicate Values

Concepts Covered

• Dictionary traversal
• Duplicate value detection
• Removing duplicate values
• Dictionary methods
• Loops
• Conditional statements
• List and dictionary operations

Learning Outcomes

After completing these programs, you will be able to:

• Find duplicate values in a dictionary.
• Remove duplicate values while keeping the first occurrence.
• Traverse dictionaries using keys and values.
• Use loops and conditions to solve dictionary problems.
• Understand how dictionaries handle unique keys and repeated values.
"""

# Find duplicate values 
data={"A":123,"B":456,"C":123,"D":789,"E" :456}
duplicates = []
for value in data.values():
    if list(data.values()).count(value) > 1 and value not in duplicates:
        duplicates.append(value)
print("Duplicate values:", duplicates)

# Remove duplicate values 
data={"A":123,"B":456,"C":123,"D":789,"E" :456}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print("Dictionary after removing duplicate values:")
print(result)
