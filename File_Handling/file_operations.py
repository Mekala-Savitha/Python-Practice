# 
FILE OPERATIONS IN PYTHON
# 


1. WHAT ARE FILE OPERATIONS?
# File operations are used to create, rename, delete, copy,move, and manage files and directories using Python.
# Python provides the os and shutil modules for performing
# file and directory operations.
import os
import shutil


2. os.rename()
# Definition:
# Renames a file or directory.

# Syntax:
# os.rename(old_name, new_name)

# Example:
import os
os.rename("old.txt", "new.txt")


3. os.remove()
# Definition:
# Deletes a file.

# Syntax:
# os.remove(file_name)

# Example:
import os
os.remove("demo.txt")
print("File removed successfully")


4. os.mkdir()
# Definition:
# Creates a single directory.

# Syntax:
# os.mkdir(directory_name)

# Example:
import os
os.mkdir("practice_folder")
print("Folder created successfully")


5. os.makedirs()
# Definition:
# Creates a directory along with all required parent directories.

# Syntax:
# os.makedirs(path)

# Example:
import os
os.makedirs("main_folder/sub_folder/examples")
print("Folders created successfully")


6. os.listdir()
# Definition:
# Returns a list containing the names of files and directories inside a specified directory.

# Syntax:
# os.listdir(path)
# If path is not provided, the current working directory is used.

# Example: Current Directory 
import os
print(os.listdir())

# For Specific Folder
import os
print(os.listdir("python_files"))

# For each item separately 
import os
for item in os.listdir():
  print(item)


7. os.rmdir()
# Definition:
# Deletes an empty directory.

# Syntax:
# os.rmdir(directory_name)

# Example:
import os
os.rmdir("empty_folder")
print("Folder deleted successfully")


8. shutil.copy()
# Definition:
# Copies a file from one location to another.

# Syntax:
# shutil.copy(source, destination)

# Example:
import shutil
shutil.copy("data.txt", "backup.txt")
print("File copied successfully")


9. shutil.move()
# Definition:
# Moves a file or directory from one location to another.

# Syntax:
# shutil.move(source, destination)

# Example:
import os
shutil.move("data.txt", "practice_folder/data.txt")
print("Folder moved successfully")


10. shutil.copytree()
# Definition:
# Copies an entire directory and all its contents to another location.

# Syntax:
# shutil.copytree(source_directory, destination_directory)

# Example:
import shutil
shutil.copytree("source_folder", "backup_folder")
print("Folder copied successfully")


11. shutil.rmtree()
# Definition:
# Deletes a directory and all files and subdirectories inside it.

# Syntax:
# shutil.rmtree(directory)

# Example:
import shutil
shutil.rmtree("backup_folder")
print("Folder deleted successfully")


12. PRACTICAL EXAMPLES

# Example 1:
# Rename a file.
with open("old.txt", "w") as file:
  file.write("Hello")
os.rename("old.txt", "new.txt")


# Example 2:
# Delete a file.
with open("demo.txt", "w") as file:
  file.write("This file will be deleted.")
os.remove("demo.txt")


# Example 3:
# Create a directory.
os.mkdir("practice_folder")
print("Directory created successfully")

# Example 4:
# Create nested directories.
os.makedirs("main_folder/sub_folder/examples")


# Example 5:
# Display all files and directories.
for item in os.listdir():
  print(item)


# Example 6:
# Delete an empty directory.
os.mkdir("empty_folder")
os.rmdir("empty_folder")


# Example 7:
# Copy a file.
with open("data.txt", "w") as file:
    file.write("Original file")
shutil.copy("data.txt", "backup.txt")
print("File copied successfully ")


# Example 8:
# Move a file.
shutil.move("backup.txt", "practice_folder/backup.txt")
print("File moved successfully")


# Example 9:
# Copy an entire directory.
os.mkdir("source_folder")
with open("source_folder/file1.txt", "w") as file:
    file.write("File 1")
shutil.copytree("source_folder", "copied_folder")
print("Folder copied successfully")


# Example 10:
# Delete a directory and all its contents.
shutil.rmtree("copied_folder")
print("Directory deleted successfully")


13. PRACTICE PROGRAMS

# Practice Program 1:
# Create a file named old_name.txt and rename it to new_name.txt.
with open("old_name.txt", "w") as file:
    file.write("This file will be renamed.")
os.rename("old_name.txt", "new_name.txt")
print("Practice 1:")
print("File renamed successfully")


# Practice Program 2:
# Create a file named delete_me.txt and delete it.
with open("delete_me.txt", "w") as file:
    file.write("This file will be deleted.")
os.remove("delete_me.txt")
print("\nPractice 2:")
print("File deleted successfully")


# Practice Program 3:
# Create a directory named practice_folder.
os.mkdir("practice_folder")
print("\nPractice 3:")
print("Directory created successfully")


# Practice Program 4:
# Create the following nested directory structure:

# main_folder/
#     sub_folder/
#         examples/
os.makedirs("main_folder/sub_folder/examples")
print("\nPractice 4:")
print("Nested directories created successfully")


# Practice Program 5:
# Display all files and directories in the current working directory.
print("\nPractice 5:")
print("Files and directories:")
for item in os.listdir():
    print(item)


# Practice Program 6:
# Create an empty directory and then delete it.
os.mkdir("empty_folder")
os.rmdir("empty_folder")
print("\nPractice 6:")
print("Empty directory deleted successfully")


# Practice Program 7:
# Create a file, copy it, move the copied file into practice_folder, and display a success message.
with open("data.txt", "w") as file:
    file.write("This is the original file.")
shutil.copy("data.txt", "backup.txt")
shutil.move("backup.txt", "practice_folder/backup.txt")
print("\nPractice 7:")
print("File copied and moved successfully")


# Practice Program 8:
# Create a directory with files inside it, copy the complete directory, and delete the copied directory.
os.makedirs("source_folder/sub_folder")
with open("source_folder/file1.txt", "w") as file:
    file.write("This is file 1.")
with open("source_folder/sub_folder/file2.txt", "w") as file:
    file.write("This is file 2.")
shutil.copytree("source_folder", "copied_folder")
print("\nPractice 8:")
print("Directory copied successfully")
shutil.rmtree("copied_folder")
print("Copied directory deleted successfully")

