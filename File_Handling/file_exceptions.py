"""

File Exception Handling in Python
=================================

This file contains 12 practical programs covering:
1. FileNotFoundError
2. PermissionError
3. FileExistsError
4. IsADirectoryError
5. try + except
6. else
7. finally
8. try + except + else + finally
9. Multiple file exceptions
10. Safe file copy
11. Safe file writing
12. Safe file reading

Note:
Run each program separately while practicing.
The input-based programs are included as examples for your GitHub
practice file.
"""

import shutil


# PROGRAM 1: FileNotFoundError
try:
    with open("missing_file.txt", "r") as file:
      content = file.read()
      
    print("File Content:")
    print(content)
  
except FileNotFoundError:
    print("Program 1: Error: File not found.")


# PROGRAM 2: PermissionError
try:
    with open("protected_file.txt", "w") as file:
        file.write("This is a test file.")

    print("Program 2: File written successfully.")

except PermissionError:
    print("Program 2: Error: Permission denied.")


# PROGRAM 3: FileExistsError
try:
    with open("student.txt", "x") as file:
        file.write("Name: Savitha")

    print("Program 3: File created successfully.")

except FileExistsError:
    print("Program 3: Error: File already exists.")


# PROGRAM 4: IsADirectoryError
try:
    with open("documents", "r") as file:
        content = file.read()

    print(content)

except IsADirectoryError:
    print(
        "Program 4: Error: The specified path is a directory, "
        "not a file."
    )


# PROGRAM 5: try + except
try:
    with open("data.txt", "r") as file:
        content = file.read()

    print("Program 5: File content:")
    print(content)

except FileNotFoundError:
    print("Program 5: Error: The file was not found.")


# PROGRAM 6: try + except + else
try:
    with open("data.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Program 6: Error: File not found.")

else:
    print("Program 6: File opened successfully.")
    print("File Content:")
    print(content)


# PROGRAM 7: try + except + finally
try:
    with open("data.txt", "r") as file:
        content = file.read()

    print("Program 7: File Content:")
    print(content)

except FileNotFoundError:
    print("Program 7: Error: File not found.")

finally:
    print("Program 7: File operation completed.")


# PROGRAM 8: try + except + else + finally
try:
    with open("data.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("Program 8: Error: File not found.")

else:
    print("Program 8: File opened successfully.")
    print("File Content:")
    print(content)

finally:
    print("Program 8: File operation finished.")


# PROGRAM 9: MULTIPLE FILE EXCEPTIONS
file_name = input("Program 9 - Enter file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except IsADirectoryError:
    print("Error: The specified path is a directory.")

except Exception as e:
    print("Unexpected error:", e)


# PROGRAM 10: SAFE FILE COPY
source = input("Program 10 - Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    shutil.copy(source, destination)

except FileNotFoundError:
    print("Error: Source file not found.")

except PermissionError:
    print("Error: Permission denied.")

except IsADirectoryError:
    print("Error: Source or destination is a directory.")

else:
    print("File copied successfully.")

finally:
    print("File copy operation completed.")


# PROGRAM 11: SAFE FILE WRITING
file_name = input("Program 11 - Enter file name: ")
content = input("Enter content to write: ")

try:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)

except PermissionError:
    print("Error: Permission denied.")

except IsADirectoryError:
    print("Error: The specified path is a directory.")

except OSError as e:
    print("File system error:", e)

else:
    print("Content written successfully.")

finally:
    print("File writing operation completed.")


# PROGRAM 12: SAFE FILE READING
file_name = input("Program 12 - Enter file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except IsADirectoryError:
    print("Error: The specified path is a directory.")

except UnicodeDecodeError:
    print("Error: File encoding could not be decoded.")

except OSError as e:
    print("File system error:", e)

else:
    print("File read successfully.")
    print("File Content:")
    print(content)

finally:
    print("File reading operation completed.")

