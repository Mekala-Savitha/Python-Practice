"""
json_files.py

Python JSON File Handling - Complete Practice File

Programs included:
1. Create and write JSON using json.dump()
2. Read JSON using json.load()
3. Convert JSON string to Python using json.loads()
4. Convert Python object to JSON string using json.dumps()
5. Python <-> JSON conversion
6. Write multiple JSON records
7. Read multiple JSON records
8. Update JSON record
9. Search JSON records
10. Delete JSON record
11. Nested JSON
12. Practical Product JSON Program
"""

import json


# PROGRAM 1: CREATE AND WRITE A JSON FILE
student = {
    "name": "Savitha",
    "age": 22,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Program 1: JSON file created successfully.")


# PROGRAM 2: READ JSON USING json.load()
with open("student.json", "r") as file:
    student = json.load(file)

print("\nProgram 2: Student Details")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# PROGRAM 3: JSON STRING TO PYTHON USING json.loads()
json_data = '{"name": "Savitha", "age": 22, "course": "Python"}'
student = json.loads(json_data)

print("\nProgram 3: JSON String to Python")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# PROGRAM 4: PYTHON TO JSON STRING USING json.dumps()
student = {
    "name": "Savitha",
    "age": 22,
    "course": "Python"
}

json_data = json.dumps(student, indent=4)

print("\nProgram 4: Python to JSON String")
print(json_data)


# PROGRAM 5: PYTHON <-> JSON CONVERSION
student = {
    "name": "Savitha",
    "age": 22,
    "course": "Python",
    "skills": ["HTML", "CSS", "Python"]
}

json_string = json.dumps(student, indent=4)

print("\nProgram 5: Python to JSON")
print(json_string)

python_data = json.loads(json_string)
print("\nJSON to Python:")
print(python_data)
print("Student Name:", python_data["name"])
print("Skills:", python_data["skills"])


# PROGRAM 6: WRITE MULTIPLE JSON RECORDS
students = [
    {"name": "Savitha", "age": 22, "course": "Python"},
    {"name": "Rahul", "age": 21, "course": "Java"},
    {"name": "Anu", "age": 20, "course": "SQL"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nProgram 6: Multiple student records written successfully.")


# PROGRAM 7: READ MULTIPLE JSON RECORDS
with open("students.json", "r") as file:
    students = json.load(file)

print("\nProgram 7: Student Records")

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("--------------------")


# PROGRAM 8: UPDATE A JSON RECORD
search_name = input("\nProgram 8 - Enter student name to update: ")
new_course = input("Enter new course: ")

with open("students.json", "r") as file:
    students = json.load(file)

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        student["course"] = new_course
        found = True
        break

if found:
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Student record updated successfully.")
else:
    print("Student not found.")


# PROGRAM 9: SEARCH JSON RECORDS
search_name = input("\nProgram 9 - Enter student name to search: ")

with open("students.json", "r") as file:
    students = json.load(file)

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent Found!")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        found = True
        break

if not found:
    print("Student not found.")


# PROGRAM 10: DELETE A JSON RECORD
delete_name = input("\nProgram 10 - Enter student name to delete: ")

with open("students.json", "r") as file:
    students = json.load(file)

original_count = len(students)

students = [
    student for student in students
    if student["name"].lower() != delete_name.lower()
]

if len(students) < original_count:
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Student record deleted successfully.")
else:
    print("Student not found.")


# PROGRAM 11: NESTED JSON
student = {
    "name": "Savitha",
    "age": 22,
    "course": "Python",
    "contact": {
        "email": "savitha@example.com",
        "phone": "9876543210"
    },
    "skills": ["Python", "HTML", "CSS"]
}

with open("nested_student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nProgram 11: Nested JSON file created successfully.")
print("Email:", student["contact"]["email"])
print("First Skill:", student["skills"][0])


# PROGRAM 12: PRACTICAL PRODUCT JSON PROGRAM
products = [
    {"id": 101, "name": "Laptop", "price": 55000, "quantity": 2},
    {"id": 102, "name": "Mouse", "price": 800, "quantity": 5},
    {"id": 103, "name": "Keyboard", "price": 1500, "quantity": 3}
]

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

print("\nProgram 12: Products saved successfully.")

with open("products.json", "r") as file:
    products = json.load(file)

total_value = 0

print("\nProduct Details:")

for product in products:
    value = product["price"] * product["quantity"]
    total_value += value

    print("ID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("Value:", value)
    print("--------------------")

print("Total Inventory Value:", total_value)

print("\nPrograms 1-12 of JSON file handling are included.")
