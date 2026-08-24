# Advanced File Handling in Python

📌 Introduction

Advanced File Handling in Python is used to work with files more efficiently by handling encoding, newlines, buffering, binary data, and large files.

Python provides built-in functions, methods, and parameters for advanced file operations.

---

📚 Topics Covered

1. File Encoding
2. UTF-8 Encoding
3. Encoding and Decoding
4. Encoding/Decoding Errors
5. newline
6. flush()
7. truncate()
8. File Buffering
9. Binary File Handling
10. Working with Large Files

---

1. File Encoding

File Encoding is the process of converting text characters into bytes so that they can be stored or transmitted.

UTF-8 is one of the most commonly used character encodings.

Syntax:

text.encode("encoding")

Example:

text = "Hello World"
data = text.encode("utf-8")

print(data)

---

2. UTF-8 Encoding

UTF-8 is a character encoding that supports Unicode characters and multiple languages.

It can represent characters such as English, Telugu, Hindi, Chinese, and many other languages.

Syntax:

open(filename, mode, encoding="utf-8")

Example:

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello తెలుగు नमस्ते")

---

3. Encoding and Decoding

Encoding converts a string into bytes.

Syntax:

text.encode("utf-8")

Decoding converts bytes back into a string.

Syntax:

data.decode("utf-8")

Example:

text = "Savitha"

encoded = text.encode("utf-8")

print(encoded)

decoded = encoded.decode("utf-8")

print(decoded)

---

4. Encoding/Decoding Errors

Encoding and decoding errors can occur when characters cannot be represented or decoded using the specified encoding.

Python provides the "errors" parameter to control how such errors are handled.

Common error handling options:

Option | Description
"strict" | Raises an error
"ignore" | Ignores unsupported characters
"replace" | Replaces unsupported characters

Syntax:

text.encode("ascii", errors="ignore")

data.decode("utf-8", errors="replace")

Example:

text = "Hello తెలుగు"

data = text.encode("ascii", errors="ignore")

print(data)

---

5. newline

The newline parameter controls how newline characters are handled when reading and writing text files.

Syntax:

open(filename, mode, newline=value)

Common values:

Value | Description
None | Uses default newline translation
"" | No newline translation
"\n" | Uses LF newline
"\r\n" | Uses CRLF newline

Example:

with open("data.txt", "w", newline="\n") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")

---

6. flush()

The flush() method forces buffered data to be written to the underlying file immediately.

It is useful when data needs to be written without waiting for the file buffer to fill.

Syntax:

file.flush()

Example:

with open("data.txt", "w") as file:
    file.write("Hello World")
    file.flush()

---

7. truncate()

The truncate() method changes the size of a file.

It can be used to reduce the file size or clear the contents of a file.

Syntax:

file.truncate()

or

file.truncate(size)

Example:

with open("data.txt", "r+") as file:
    file.truncate(5)

To clear a file:

with open("data.txt", "r+") as file:
    file.truncate(0)

---

8. File Buffering

File Buffering is the process of temporarily storing data in memory before it is read from or written to a file.

Buffering can improve file input and output performance.

Syntax:

open(filename, mode, buffering=value)

Common values:

Value | Description
-1 | Default buffering
0 | Unbuffered binary I/O
1 | Line buffering
Positive integer | Buffer size

Example:

with open("data.bin", "wb", buffering=1024) as file:
    file.write(b"Hello World")
    file.flush()

---

9. Binary File Handling

Binary File Handling is used to read and write files as raw bytes instead of normal text.

Binary files include:

- Images
- Videos
- Audio files
- PDF files
- Executable files

Binary File Modes:

Mode | Description
"rb" | Read binary
"wb" | Write binary
"ab" | Append binary

Example:

with open("data.bin", "wb") as file:
    file.write(b"Hello World")

Reading a binary file:

with open("data.bin", "rb") as file:
    data = file.read()

print(data)

---

10. Working with Large Files

Working with Large Files means processing large files efficiently without loading the entire file into memory.

Large files can be processed:

- Line by line
- In chunks

---

10.1 Reading Large Text Files Line by Line

Syntax:

with open(filename, "r") as file:
    for line in file:
        statements

Example:

with open("large_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")

---

10.2 Reading Large Files in Chunks

A chunk is a small portion of a file processed at a time.

Syntax:

while True:
    chunk = file.read(size)

    if not chunk:
        break

    statements

Example:

with open("large_text.txt", "r", encoding="utf-8") as file:
    while True:
        chunk = file.read(1024)

        if not chunk:
            break

        print(chunk, end="")

---

10.3 Large Binary File Copying

Large binary files can be copied using chunks instead of loading the entire file into memory.

Example:

with open("large_video.mp4", "rb") as source:
    with open("large_video_copy.mp4", "wb") as destination:

        while True:
            chunk = source.read(1024 * 1024)

            if not chunk:
                break

            destination.write(chunk)

---

📌 Important Points

- UTF-8 is commonly used for Unicode text.
- encode() converts strings into bytes.
- decode() converts bytes into strings.
- newline controls newline handling.
- flush() writes buffered data immediately.
- truncate() changes the size of a file.
- Buffering temporarily stores file data in memory.
- Binary files are handled using bytes.
- Large files should be processed line by line or in chunks.
- Chunk processing helps reduce memory usage.

---

🎯 Learning Outcome

After completing Advanced File Handling, I can:

- Work with UTF-8 encoded files.
- Encode and decode strings.
- Handle encoding and decoding errors.
- Control newline behavior.
- Flush file buffers.
- Truncate files.
- Work with file buffering.
- Read and write binary files.
- Copy binary files using chunks.
- Process large files efficiently.
