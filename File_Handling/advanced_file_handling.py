"""
Advanced File Handling in Python
================================

Topics Covered:
1. File Encoding
2. UTF-8 Encoding and Decoding
3. Encoding/Decoding Errors
4. newline Parameter
5. flush()
6. truncate()
7. File Buffering
8. Binary File Handling
9. Working with Large Files
"""


# 1. FILE ENCODING

# 1.1 String to Bytes using UTF-8

text = "Hello World"
data = text.encode("utf-8")

print(data)
print(type(data))


# 1.2 Encoding Unicode Text

text = "Hello\nनमस्ते\nతెలుగు"
data = text.encode("utf-8")

print(data)
print(type(data))


# 1.3 Bytes to String using UTF-8

data = b"Savitha"
text = data.decode("utf-8")

print(text)
print(type(text))


# 1.4 Reading a UTF-8 Text File

with open("message.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)


# 1.5 Writing UTF-8 Text

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello World\n")
    file.write("नमस्ते\n")
    file.write("తెలుగు")


# 1.6 Reading UTF-8 Text

with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)


# 1.7 Appending UTF-8 Text

with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nGood Morning")


# 2. ENCODING AND DECODING ERRORS

# 2.1 ASCII Encoding with errors="ignore"

text = "Hello తెలుగు"
data = text.encode("ascii", errors="ignore")
print(data)


# 2.2 ASCII Encoding with errors="replace"

data = text.encode("ascii", errors="replace")
print(data)


# 2.3 UTF-8 Decoding with errors="ignore"

data = b"Hello \xff World"
text = data.decode("utf-8", errors="ignore")

print(text)


# 2.4 UTF-8 Decoding with errors="replace"

data = b"Hello \xff World"
text = data.decode("utf-8", errors="replace")
print(text)


# 3. NEWLINE PARAMETER

# 3.1 newline="\n"

with open("newline_demo.txt", "w", newline="\n") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


# 3.2 newline=""

with open("newline_demo.txt", "w", newline="", encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


# 3.3 newline=None

with open("newline_default.txt", "w", newline=None, encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


# 3.4 newline="\r\n"

with open("newline_default.txt", "w", newline="\r\n", encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


# 3.5 Reading with newline=""

with open("newline_default.txt", "r", newline="", encoding="utf-8") as file:
    data = file.read()
print(repr(data))


# 4. flush()

# 4.1 Basic flush()

with open("flush_demo.txt", "w", encoding="utf-8") as file:
    file.write("Hello World")
    file.flush()


# 4.2 Multiple flush() calls

with open("flush_demo.txt", "w", encoding="utf-8") as file:
    file.write("First Line\n")
    file.flush()

    file.write("Second Line\n")
    file.flush()

    file.write("Third Line\n")
    file.flush()


# 4.3 Progress-style writing

with open("progress.txt", "w", encoding="utf-8") as file:
    for i in range(1, 6):
        file.write(f"Processing {i}\n")
        file.flush()


# 5. truncate()

# 5.1 truncate(size)

# If truncate_demo.txt contains:
# Hello World

with open("truncate_demo.txt", "r+") as file:
    file.truncate(5)


# 5.2 truncate() at current file position

# If truncate_demo.txt contains:
# Hello World

with open("truncate_demo.txt", "r+") as file:
    file.read(5)
    file.truncate()


# 5.3 Clear a file using truncate(0)

with open("clear_demo.txt", "r+") as file:
    file.truncate(0)


# 5.4 Practical log file example

with open("application.log", "r+") as file:
    file.truncate(0)
    file.write("Log file cleared")


# IMPORTANT:
# truncate(size) works with the file's byte/file position.
# It should not be treated as a character-count operation
# when working with multibyte UTF-8 characters.


# ============================================================
# 6. FILE BUFFERING
# ============================================================

# 6.1 Default buffering

with open("buffer_demo.txt", "w", encoding="utf-8") as file:
    print("File opened")
    print("Writing data...")

    file.write("Hello World")
    print("Data written")

    file.flush()

    print("Buffer flushed")


# 6.2 Buffered binary file

with open("buffer_demo.bin", "wb", buffering=1024) as file:
    file.write(b"Hello World")
    file.flush()


# 6.3 Unbuffered binary file

with open("unbuffered.bin", "wb", buffering=0) as file:
    file.write(b"Hello World")


# 6.4 Line buffering

with open("line_buffer.txt", "w", buffering=1, encoding="utf-8") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")


# 6.5 Buffered binary writing

with open("buffered.bin", "wb", buffering=1024) as file:
    file.write(b"Hello")
    file.write(b" World")
    file.flush()


# 7. BINARY FILE HANDLING

# 7.1 Write binary data

with open("binary_demo.bin", "wb") as file:
    file.write(b"Hello Binary World")


# 7.2 Read binary data

with open("binary_demo.bin", "rb") as file:
    data = file.read()

print(data)
print(type(data))


# 7.3 Convert binary data to text

with open("binary_demo.bin", "rb") as file:
    data = file.read()

text = data.decode("utf-8")

print(text)
print(type(text))


# 7.4 Append binary data

with open("binary_demo.bin", "ab") as file:
    file.write(b" - Python")


# 7.5 Copy a binary file

with open("binary_demo.bin", "rb") as source:
    data = source.read()

with open("binary_copy.bin", "wb") as destination:
    destination.write(data)


# 7.6 Copy binary file using chunks

with open("binary_demo.bin", "rb") as source:
    with open("binary_copy2.bin", "wb") as destination:

        while True:
            chunk = source.read(1024)

            if not chunk:
                break

            destination.write(chunk)


# 7.7 Display size of each binary chunk

with open("binary_demo.bin", "rb") as source:
    with open("binary_copy3.bin", "wb") as destination:

        while True:
            chunk = source.read(1024)

            if not chunk:
                break

            print("Chunk size:", len(chunk))

            destination.write(chunk)


# 8. WORKING WITH LARGE FILES

# 8.1 Read a large text file line by line

with open("large_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")


# 8.2 Read a large text file in chunks

with open("large_text.txt", "r", encoding="utf-8") as file:

    while True:
        chunk = file.read(1024)

        if not chunk:
            break

        print(chunk, end="")


# 8.3 Count lines without loading the entire file

count = 0

with open("large_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Total lines:", count)


# 8.4 Search for a word in a large file

with open("large_text.txt", "r", encoding="utf-8") as file:

    for line_number, line in enumerate(file, start=1):

        if "Python" in line:
            print(f"Line {line_number}: {line}", end="")


# 8.5 Copy a large binary file using 1 MB chunks

with open("large_video.mp4", "rb") as source:
    with open("large_video_copy.mp4", "wb") as destination:

        while True:
            chunk = source.read(1024 * 1024)

            if not chunk:
                break

            destination.write(chunk)


# 8.6 Large file copy with total byte count

total_copied = 0

with open("large_video.mp4", "rb") as source:
    with open("large_video_copy2.mp4", "wb") as destination:

        while True:
            chunk = source.read(1024 * 1024)

            if not chunk:
                break

            destination.write(chunk)

            total_copied += len(chunk)

print("Total bytes copied:", total_copied)

