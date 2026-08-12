"""
different_data_files.py

Python File Handling - Reading & Writing Different Data
Topics covered:
1. Text file writing
2. Text file reading
3. Text file appending
4. Counting lines, words and characters
5. Reading binary data using rb
6. Writing binary data using wb
7. Appending binary data using ab
8. Copying an image using binary mode
9. Copying a large binary file using chunks
10. Text <-> bytes conversion
"""


# PROGRAM 1: CREATE AND WRITE A TEXT FILE
with open("student.txt", "w") as file:
    file.write("Name: Student\n")
    file.write("Course: Python Full Stack\n")
    file.write("Topic: File Handling\n")

print("Program 1: Data written successfully.")


# PROGRAM 2: READ A TEXT FILE
with open("student.txt", "r") as file:
    data = file.read()
print("\nProgram 2: File Content:")
print(data)


# PROGRAM 3: APPEND DATA TO A TEXT FILE
with open("student.txt", "a") as file:
    file.write("Status: Learning Python\n")
print("Program 3: Data appended successfully.")


# PROGRAM 4: COUNT LINES, WORDS AND CHARACTERS
with open("student.txt", "r") as file:
    data = file.read()
lines = data.splitlines()
words = data.split()
characters = len(data)
print("\nProgram 4: File Statistics")
print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)


# PROGRAM 5: READ A BINARY FILE USING rb
# Keep photo.jpg in the same folder as this Python file.
try:
    with open("photo.jpg", "rb") as file:
        data = file.read()
    print("\nProgram 5: Binary file read successfully.")
    print("Data type:", type(data))
    print("File size:", len(data), "bytes")
except FileNotFoundError:
    print("\nProgram 5: photo.jpg not found. Add an image to test this program.")


# PROGRAM 6: WRITE BINARY DATA USING wb
data = b"Hello Python\nThis is binary data."
with open("data.bin", "wb") as file:
    file.write(data)
print("\nProgram 6: Binary data written successfully.")


# PROGRAM 7: APPEND BINARY DATA USING ab
data = b"\nThis data was appended using ab mode."
with open("data.bin", "ab") as file:
    file.write(data)
print("Program 7: Binary data appended successfully.")
with open("data.bin", "rb") as file:
    data = file.read()
print("Updated binary data:", data)


# PROGRAM 8: COPY AN IMAGE USING BINARY MODE
# Keep photo.jpg in the same folder as this Python file.
try:
    with open("photo.jpg", "rb") as source:
        data = source.read()
    with open("photo_copy.jpg", "wb") as destination:
        destination.write(data)
    print("\nProgram 8: Image copied successfully.")
except FileNotFoundError:
    print("\nProgram 8: photo.jpg not found. Add an image to test this program.")


# PROGRAM 9: COPY A LARGE BINARY FILE USING CHUNKS
# Reads 1024 bytes at a time instead of loading the whole file.
try:
    with open("photo.jpg", "rb") as source:
        with open("photo_copy_chunks.jpg", "wb") as destination:
            while True:
                data = source.read(1024)
                if not data:
                    break
                destination.write(data)
    print("Program 9: File copied successfully using chunks.")
except FileNotFoundError:
    print("Program 9: photo.jpg not found. Add an image to test this program.")


# PROGRAM 10: TEXT TO BYTES AND BYTES TO TEXT
text = "Hello Python"
# Text -> Bytes
data = text.encode("utf-8")
print("\nProgram 10: Text to Bytes")
print("Bytes:", data)
print("Type:", type(data))

# Bytes -> Text
new_text = data.decode("utf-8")
print("Bytes to Text:", new_text)
print("Type:", type(new_text))

