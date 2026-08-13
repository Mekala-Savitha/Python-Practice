"""
csv_files.py
Python CSV File Handling - Complete Practice File

Topics:
1. Create and write CSV
2. writerow()
3. writerows()
4. csv.reader()
5. Reading individual fields
6. DictReader
7. DictWriter
8. Search records
9. Update records
10. Calculate CSV data
11. Student CSV Record System
12. Employee CSV Record System
13. Student Management System
"""

import csv

# PROGRAM 1: CREATE AND WRITE A CSV FILE
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Savitha", 22, "Python"])
    writer.writerow(["Rahul", 21, "Java"])
    writer.writerow(["Anu", 20, "SQL"])
print("Program 1: CSV file created successfully.")


# PROGRAM 2: WRITE MULTIPLE ROWS USING writerows()
students = [
    ["Name", "Age", "Course"],
    ["Savitha", 22, "Python"],
    ["Rahul", 21, "Java"],
    ["Anu", 20, "SQL"],
    ["Priya", 23, "HTML"]
]
with open("students2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("Program 2: Multiple rows written successfully.")


# PROGRAM 3: READ CSV USING csv.reader()
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    print("\nProgram 3: CSV Rows")
    for row in reader:
        print(row)


# PROGRAM 4: READ INDIVIDUAL CSV FIELDS
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    print("\nProgram 4: Individual Fields")
    for row in reader:
        print("Name:", row[0])
        print("Age:", row[1])
        print("Course:", row[2])
        print("--------------------")


# PROGRAM 5: READ CSV USING DictReader
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    print("\nProgram 5: DictReader")
    for row in reader:
        print("Name:", row["Name"])
        print("Age:", row["Age"])
        print("Course:", row["Course"])


# PROGRAM 6: WRITE CSV USING DictWriter
students = [
    {"Name": "Savitha", "Age": 22, "Course": "Python"},
    {"Name": "Rahul", "Age": 21, "Course": "Java"},
    {"Name": "Anu", "Age": 20, "Course": "SQL"}
]

with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Course"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
print("\nProgram 6: DictWriter completed.")


# PROGRAM 7: SEARCH FOR A STUDENT
search_name = input("\nProgram 7 - Enter student name to search: ")
found = False

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].lower() == search_name.lower():
            print("Student Found!")
            print("Name:", row["Name"])
            print("Age:", row["Age"])
            print("Course:", row["Course"])
            found = True
            break

if not found:
    print("Student not found.")
    
    
# PROGRAM 8: UPDATE A STUDENT RECORD
search_name = input("\nProgram 8 - Enter student name to update: ")
new_course = input("Enter new course: ")

students = []
found = False

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].lower() == search_name.lower():
            row["Course"] = new_course
            found = True
        students.append(row)

if found:
    with open("students.csv", "w", newline="") as file:
        fieldnames = ["Name", "Age", "Course"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print("Student record updated successfully.")
else:
    print("Student not found.")


# PROGRAM 9: DELETE A STUDENT RECORD
delete_name = input("\nProgram 9 - Enter student name to delete: ")

students = []
found = False

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].lower() == delete_name.lower():
            found = True
            continue
        students.append(row)

if found:
    with open("students.csv", "w", newline="") as file:
        fieldnames = ["Name", "Age", "Course"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print("Student record deleted successfully.")
else:
    print("Student not found.")


# PROGRAM 10: CALCULATE DATA FROM CSV
total_age = 0
student_count = 0

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_age += int(row["Age"])
        student_count += 1

print("\nProgram 10: CSV Statistics")

if student_count > 0:
    print("Number of students:", student_count)
    print("Total age:", total_age)
    print("Average age:", total_age / student_count)
else:
    print("No student records found.")


# PROGRAM 11: STUDENT CSV RECORD SYSTEM
FILE_NAME = "student_records.csv"

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow([name, age, course])

    print("Student added successfully.")


def view_students():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            for row in csv.reader(file):
                print(row)
    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_name = input("Enter student name: ")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            for row in csv.reader(file):
                if row[0].lower() == search_name.lower():
                    print("Student found!")
                    print("Name:", row[0])
                    print("Age:", row[1])
                    print("Course:", row[2])
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")


# PROGRAM 12: EMPLOYEE CSV RECORD SYSTEM
EMPLOYEE_FILE = "employees.csv"

def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    with open(EMPLOYEE_FILE, "a", newline="") as file:
        csv.writer(file).writerow(
            [employee_id, name, department, salary]
        )

    print("Employee added successfully.")


def view_employees():
    try:
        with open(EMPLOYEE_FILE, "r", newline="") as file:
            for row in csv.reader(file):
                print(row)
    except FileNotFoundError:
        print("No employee records found.")


def search_employee():
    search_id = input("Enter Employee ID: ")

    try:
        with open(EMPLOYEE_FILE, "r", newline="") as file:
            for row in csv.reader(file):
                if row[0] == search_id:
                    print("Employee Found!")
                    print("ID:", row[0])
                    print("Name:", row[1])
                    print("Department:", row[2])
                    print("Salary:", row[3])
                    return
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")


def calculate_average_salary():
    total_salary = 0
    employee_count = 0

    try:
        with open(EMPLOYEE_FILE, "r", newline="") as file:
            for row in csv.reader(file):
                total_salary += float(row[3])
                employee_count += 1

        if employee_count:
            print("Average Salary:", total_salary / employee_count)
        else:
            print("No employee records found.")

    except FileNotFoundError:
        print("No employee records found.")


# PROGRAM 13: COMPLETE STUDENT MANAGEMENT SYSTEM
MANAGEMENT_FILE = "student_management.csv"
FIELDNAMES = ["ID", "Name", "Age", "Course"]

def management_add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(MANAGEMENT_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Course": course
        })

    print("Student added successfully.")


def management_view_students():
    try:
        with open(MANAGEMENT_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n===== STUDENT RECORDS =====")

            for row in reader:
                print(
                    f"ID: {row['ID']} | "
                    f"Name: {row['Name']} | "
                    f"Age: {row['Age']} | "
                    f"Course: {row['Course']}"
                )

    except FileNotFoundError:
        print("No student records found.")


def management_search_student():
    search_id = input("Enter Student ID: ")

    try:
        with open(MANAGEMENT_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["ID"] == search_id:
                    print("\nStudent Found!")
                    print("ID:", row["ID"])
                    print("Name:", row["Name"])
                    print("Age:", row["Age"])
                    print("Course:", row["Course"])
                    return

            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")

def management_update_student():
    search_id = input("Enter Student ID to update: ")

    students = []
    found = False

    try:
        with open(MANAGEMENT_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["ID"] == search_id:
                    row["Name"] = input("Enter new name: ")
                    row["Age"] = input("Enter new age: ")
                    row["Course"] = input("Enter new course: ")
                    found = True

                students.append(row)

        if found:
            with open(MANAGEMENT_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(students)

            print("Student updated successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def management_delete_student():
    delete_id = input("Enter Student ID to delete: ")

    students = []
    found = False

    try:
        with open(MANAGEMENT_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["ID"] == delete_id:
                    found = True
                    continue

                students.append(row)

        if found:
            with open(MANAGEMENT_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(students)

            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")
