"""
Dictionary Searching

This file contains programs for searching and filtering data in Python
dictionaries. These programs help locate values, compare dictionaries,
and filter dictionary data based on keys or values.

Programs Included

1. Search for a Value
2. Find Common Values
3. Find Common Key-Value Pairs
4. Filter Dictionary by Key
5. Filter Dictionary by Value

Concepts Covered

• Dictionary searching
• Searching values
• Common values
• Common key-value pairs
• Dictionary filtering
• Dictionary traversal
• Loops
• Conditional statements

Learning Outcomes

After completing these programs, you will be able to:

• Search for values in a dictionary.
• Find common values between two dictionaries.
• Find common key-value pairs.
• Filter dictionaries using keys.
• Filter dictionaries using values.
• Apply loops and conditions to search and filter dictionary data.
"""

# Search for a value 
student = {
    "name":"Savitha",
    "age":22,
    "city":"Hyderabad", 
    "branch":"CSE"
}
value=input("Enter a value:")
if value in student.values():
  print("Found")
else:
  print("Not Found") 

# Find common values
data1={"name":"savitha", "age":22,"branch":"CSE"}
data2={"college":"SCTC", "marks":96,"name":"savitha"}
for value in data1.values():
    if value in data2.values():
        print(value)    

# Find common key-value pairs 
data1={"name":"savitha", "age":22,"branch":"CSE"}
data2={"college":"SCTC", "marks":96,"name":"savitha"}
for key,value in data1.items():
    if (key,value) in data2.items():
        print(key,value)     

# Filter dictionary by key
student={
    "name":"Savitha",
    "age":22,
    "branch":"CSE",
    "city":"Hyderabad"
}
result={}
for key,value in student.items():
    if key=="branch":
        result[key]=value
print(result)

# Filter dictionary by value
student = {
    "name":"Savitha",
    "age":22,
    "branch":"CSE",
    "city":"Hyderabad"
}
result={}
for key,value in student.items():
    if value=="Savitha":
        result[key]=value
print(result)      
