Python File Handling

📌 Introduction

File Handling in Python is used to create, open, read, write, append, and manage files.

Python provides built-in functions and methods to work with files efficiently.

---

📚 Topics Covered

1. "open()"

Used to open a file.

Syntax:

open(filename, mode)

---

2. File Modes

File modes specify the operation to perform on a file.

Mode| Description
"r"| Read
"w"| Write and overwrite
"a"| Append
"x"| Create a new file

---

3. "read()"

Used to read the contents of a file.

Syntax:

file.read()

---

4. "readline()"

Used to read one line from a file.

Syntax:

file.readline()

---

5. "readlines()"

Used to read all lines from a file and return them as a list.

Syntax:

file.readlines()

---

6. "write()"

Used to write data into a file.

Syntax:

file.write(data)

---

7. "writelines()"

Used to write multiple strings into a file.

Syntax:

file.writelines(iterable)

---

8. "close()"

Used to close an opened file.

Syntax:

file.close()

---

9. "with open()"

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

📊 Quick Reference

Concept| Purpose
"open()"| Open a file
"r"| Read
"w"| Write / Overwrite
"a"| Append
"x"| Create
"read()"| Read entire content
"readline()"| Read one line
"readlines()"| Read all lines
"write()"| Write data
"writelines()"| Write multiple lines
"close()"| Close file
"with open()"| Safely handle files

---

🎯 Learning Goals

After completing this topic, I should be able to:

- Open and close files
- Understand file modes
- Read file contents
- Read individual and multiple lines
- Write data to files
- Append data to files
- Create new files
- Use "with open()" for safe file handling

---
