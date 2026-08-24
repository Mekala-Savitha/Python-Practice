Python File Handling

📌 Introduction

File Handling in Python is used to create, open, read, write, append, and manage files.

Python provides built-in functions and methods to work with files efficiently.

---

📚 Topics Covered

# 1. "open()"

Used to open a file.

Syntax:

open(filename, mode)

---

# 2. File Modes

File modes specify the operation to perform on a file.

Mode| Description
"r"| Read
"w"| Write and overwrite
"a"| Append
"x"| Create a new file

---

# 3. "read()"

Used to read the contents of a file.

Syntax:

file.read()

---

# 4. "readline()"

Used to read one line from a file.

Syntax:

file.readline()

---

# 5. "readlines()"

Used to read all lines from a file and return them as a list.

Syntax:

file.readlines()

---

# 6. "write()"

Used to write data into a file.

Syntax:

file.write(data)

---

# 7. "writelines()"

Used to write multiple strings into a file.

Syntax:

file.writelines(iterable)

---

# 8. "close()"

Used to close an opened file.

Syntax:

file.close()

---

# 9. "with open()"

Used to work with files safely. Python automatically closes the file after the "with" block.

Syntax:

with open(filename, mode) as file:
    statements

---

🔄 Basic File Handling Process

Open File
    ↓
Perform Operation
    ↓
Read / Write / Append
    ↓
Close File

---

# 10. File Paths

File paths specify the location of files and directories.

Python supports both relative and absolute paths.

---

# 10.1 Relative Path

A relative path specifies the location relative to the current working directory.

Example:

open("data.txt", "r")

---

# 10.2 Absolute Path

An absolute path specifies the complete location of a file.

Example:

open("C:/Users/User/Documents/data.txt", "r")

---

# 10.3 os Module

The `os` module provides functions for working with files and directories.

Syntax:

import os

Example:

import os

print(os.getcwd())

---

# 10.4 Current Working Directory

`os.getcwd()` returns the current working directory.

Syntax:

os.getcwd()

Example:

import os

print(os.getcwd())

---

 10.5 Change Working Directory

`os.chdir()` changes the current working directory.

Syntax:

os.chdir(path)

Example:

import os

os.chdir("C:/Users/User/Documents")

---

# 10.6 Check Whether a Path Exists

`os.path.exists()` checks whether a file or directory exists.

Syntax:

os.path.exists(path)

Example:

import os

print(os.path.exists("data.txt"))

---

# 10.7 Check File or Directory

`os.path.isfile()` checks whether a path is a file.

Syntax:

os.path.isfile(path)

`os.path.isdir()` checks whether a path is a directory.

Syntax:

os.path.isdir(path)

Example:

import os

print(os.path.isfile("data.txt"))
print(os.path.isdir("Documents"))

---

# 11. File Pointer

A file pointer represents the current position within a file.

Python provides `tell()` and `seek()` to work with the file pointer.

---

# 11.1 tell()

The `tell()` method returns the current position of the file pointer.

Syntax:

file.tell()

Example:

with open("data.txt", "r") as file:
    print(file.tell())

---

# 11.2 seek()

The `seek()` method moves the file pointer to a specific position.

Syntax:

file.seek(position)

Example:

with open("data.txt", "r") as file:
    file.seek(5)
    data = file.read()

print(data)

---

# 11.3 tell() and seek() Together

Example:

with open("data.txt", "r") as file:
    print(file.tell())

    file.read(5)

    print(file.tell())

    file.seek(0)

    print(file.tell())

---

# 12. File Exception Handling

File operations can produce errors when a file does not exist, access is denied, or an incorrect operation is performed.

Python provides exception handling using:

- `try`
- `except`
- `else`
- `finally`

---

# 12.1 FileNotFoundError

Occurs when the specified file does not exist.

Syntax:

try:
    file_operation()
except FileNotFoundError:
    statements

Example:

try:
    with open("missing.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")

---

# 12.2 PermissionError

Occurs when the program does not have permission to perform the requested file operation.

Syntax:

try:
    file_operation()
except PermissionError:
    statements

---

# 12.3 FileExistsError

Occurs when an operation tries to create a file or directory that already exists.

Syntax:

try:
    file_operation()
except FileExistsError:
    statements

---

# 12.4 IsADirectoryError

Occurs when a directory is used where a file is expected.

Syntax:

try:
    file_operation()
except IsADirectoryError:
    statements

---

# 12.5 try + except

Used to handle file-related exceptions.

Syntax:

try:
    statements
except Exception:
    statements

---

# 12.6 try + except + else

The `else` block executes when no exception occurs.

Syntax:

try:
    statements
except Exception:
    statements
else:
    statements

---

# 12.7 try + except + finally

The `finally` block executes whether an exception occurs or not.

Syntax:

try:
    statements
except Exception:
    statements
finally:
    statements

---

# 12.8 try + except + else + finally

All four blocks can be combined.

Syntax:

try:
    statements
except Exception:
    statements
else:
    statements
finally:
    statements

---

# 12.9 Multiple File Exceptions

Multiple exceptions can be handled using multiple `except` blocks.

Example:

try:
    with open("data.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

---

# 12.10 Safe File Operations

Exception handling can be used to safely perform:

- File reading
- File writing
- File copying
- File creation

Example:

try:
    with open("data.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File does not exist")

---

# 13. CSV Files

CSV stands for Comma-Separated Values.

CSV files are commonly used to store tabular data such as student records, employee information, and product data.

Python provides the built-in `csv` module for working with CSV files.

---

# 13.1 Import csv

Syntax:

import csv

---

# 13.2 Read a CSV File

The `csv.reader()` function reads rows from a CSV file.

Syntax:

csv.reader(file)

Example:

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

---

# 13.3 Write a CSV File

The `csv.writer()` function is used to write data into a CSV file.

Syntax:

csv.writer(file)

Example:

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Savitha", 23, 85])

---

# 13.4 writerow()

`writerow()` writes one row to a CSV file.

Syntax:

writer.writerow(row)

---

# 13.5 writerows()

`writerows()` writes multiple rows to a CSV file.

Syntax:

writer.writerows(rows)

Example:

import csv

rows = [
    ["Name", "Age"],
    ["Savitha", 23],
    ["Rahul", 24]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

---

# 13.6 DictReader

`DictReader` reads CSV rows as dictionaries.

Syntax:

csv.DictReader(file)

Example:

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

---

# 13.7 DictWriter

`DictWriter` writes dictionaries into a CSV file.

Syntax:

csv.DictWriter(file, fieldnames)

Example:

import csv

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "Name": "Savitha",
        "Age": 23
    })

---

# 14. Different Data Files

Python can work with different types of data files.

Common file types include:

File Type | Purpose
TXT | Text data
CSV | Tabular data
JSON | Structured data
BIN | Binary data

Different file formats are useful for different applications.

---

# 14.1 Text Files

Text files store human-readable text.

Example:

data.txt

---

# 14.2 CSV Files

CSV files store tabular data in rows and columns.

Example:

students.csv

---

# 14.3 JSON Files

JSON files store structured data using key-value pairs, lists, and nested structures.

Example:

students.json

---

# 14.4 Binary Files

Binary files store data as bytes.

Example:

image.jpg
video.mp4
data.bin

---

# 15. JSON Files

JSON stands for JavaScript Object Notation.

JSON is a lightweight format commonly used for storing and exchanging structured data.

Python provides the built-in `json` module for working with JSON.

---

# 15.1 Import json

Syntax:

import json

---

# 15.2 Python Objects and JSON

Python data can be converted into JSON format.

Common Python to JSON conversions:

Python | JSON
dict | object
list | array
str | string
int | number
float | number
True | true
False | false
None | null

---

# 15.3 json.dump()

`json.dump()` writes Python data into a JSON file.

Syntax:

json.dump(data, file)

Example:

import json

student = {
    "name": "Savitha",
    "age": 23,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)

---

# 15.4 json.load()

`json.load()` reads JSON data from a file and converts it into a Python object.

Syntax:

json.load(file)

Example:

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)

---

# 15.5 json.dumps()

`json.dumps()` converts a Python object into a JSON formatted string.

Syntax:

json.dumps(data)

Example:

import json

student = {
    "name": "Savitha",
    "age": 23
}

data = json.dumps(student)

print(data)

---

# 15.6 json.loads()

`json.loads()` converts a JSON formatted string into a Python object.

Syntax:

json.loads(string)

Example:

import json

data = '{"name": "Savitha", "age": 23}'

student = json.loads(data)

print(student)

---

# 15.7 JSON File Operations

Common JSON operations include:

- Create JSON files
- Read JSON files
- Write JSON data
- Update JSON data
- Append data to JSON structures
- Convert Python objects to JSON
- Convert JSON to Python objects

---

# 15.8 JSON Data Flow

Python Object
       ↓
json.dump()
       ↓
JSON File

JSON File
       ↓
json.load()
       ↓
Python Object

Python Object
       ↓
json.dumps()
       ↓
JSON String

JSON String
       ↓
json.loads()
       ↓
Python Object

---

📊 Quick Reference

Concept | Purpose

"open()" | Open a file
"read()" | Read file content
"readline()" | Read one line
"readlines()" | Read all lines
"write()" | Write data
"writelines()" | Write multiple strings
"close()" | Close file
"with open()" | Safely handle files
"os.getcwd()" | Get current directory
"os.chdir()" | Change directory
"os.path.exists()" | Check path existence
"os.path.isfile()" | Check whether path is a file
"os.path.isdir()" | Check whether path is a directory
"tell()" | Get file pointer position
"seek()" | Move file pointer
"try" | Test code for exceptions
"except" | Handle exceptions
"csv.reader()" | Read CSV data
"csv.writer()" | Write CSV data
"DictReader" | Read CSV rows as dictionaries
"DictWriter" | Write dictionaries to CSV
"json.dump()" | Write JSON to file
"json.load()" | Read JSON from file
"json.dumps()" | Convert Python object to JSON string
"json.loads()" | Convert JSON string to Python object

---

🎯 Learning Goals

After completing this section, I should be able to:

- Open and close files
- Understand file modes
- Read and write files
- Append data to files
- Work with file paths
- Use absolute and relative paths
- Use the os module for file operations
- Control the file pointer using tell() and seek()
- Handle file-related exceptions
- Safely read, write, and copy files
- Read and write CSV files
- Work with DictReader and DictWriter
- Understand different data file formats
- Read and write JSON files
- Convert Python objects to and from JSON

