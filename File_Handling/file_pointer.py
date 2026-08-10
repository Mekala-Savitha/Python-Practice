# 
FILE POINTER IN PYTHON
# 


1. WHAT IS A FILE POINTER?
# A file pointer represents the current position in a file.
# It determines where the next read or write operation occurs.
#
# When a file is opened, the pointer starts at position 0.


2. tell()
# tell() returns the current position of the file pointer.
# Syntax:
# file.tell()

# Example 1: Initial position
with open("data.txt", "r") as file:
    print("Initial position:", file.tell())


# Example 2: Position after reading
with open("data.txt", "r") as file:
    file.read(6)
    print("Current position:", file.tell())


# Example 3: Pointer movement
with open("data.txt", "r") as file:
    print("Position:", file.tell())
    file.read(3)
    print("After reading 3 characters:", file.tell())
    file.read(5)
    print("After reading 5 more characters:", file.tell())


3. seek()
# seek() moves the file pointer to a specified position.
# Syntax:
# file.seek(position)

# Example 1: Move pointer to the beginning

with open("data.txt", "r") as file:
    file.read(5)
    print("Before seek:", file.tell())
    file.seek(0)
    print("After seek:", file.tell())


# Example 2: Move pointer to position 7
with open("data.txt", "r") as file:
    file.seek(7)
    print(file.read())


# Example 3: Read the same content again
with open("data.txt", "r") as file:
    print("First read:")
    print(file.read(5))
    file.seek(0)
    print("Second read:")
    print(file.read(5))


4. PRACTICAL EXAMPLES

# Example 1: Read first 5 characters and read them again
with open("data.txt", "r") as file:
    first = file.read(5)
    print("First read:", first)
    file.seek(0)
    second = file.read(5)
    print("Second read:", second)


# Example 2: Skip the first 5 characters
with open("data.txt", "r") as file:
    file.seek(5)
    print("Content after position 5:")
    print(file.read())


# Example 3: Display pointer movement
with open("data.txt", "r") as file:
    print("Starting position:", file.tell())
    file.read(10)
    print("After reading 10 characters:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())


# Example 4: Read from a particular position
with open("data.txt", "r") as file:
    file.seek(10)
    print("Content from position 10:")
    print(file.read())


# Example 5: Reset the pointer
with open("data.txt", "r") as file:
    print("First:", file.read(5))
    file.seek(0)
    print("After reset:", file.read(5))


5. PRACTICE PROGRAMS

# Practice Program 1:
# Display the initial position of the file pointer.
with open("data.txt", "r") as file:
    print("Initial position:", file.tell())


# Practice Program 2:
# Read 10 characters and display the current position.
with open("data.txt", "r") as file:
    file.read(10)
    print("Current position:", file.tell())


# Practice Program 3:
# Move the pointer to position 5 and display
# the remaining contents.
with open("data.txt", "r") as file:
    file.seek(5)
    print(file.read())


# Practice Program 4:
# Read the first 5 characters, move the pointer
# back to position 0, and read them again.
with open("data.txt", "r") as file:
    file.read(5)
    print("Position:", file.tell())
    file.seek(0)
    print(file.read(5))


# Practice Program 5:
# Display the pointer position before and after
# reading 10 characters.
with open("data.txt", "r") as file:
    print("Before reading:", file.tell())
    file.read(10)
    print("After reading:", file.tell())


# Practice Program 6:
# Move the pointer to position 8 and read
# the remaining contents.
with open("data.txt", "r") as file:
    file.seek(8)
    print(file.read())


# Practice Program 7:
# Read 5 characters, display the pointer position,
# reset the pointer using seek(0), and display
# the position again.
with open("data.txt", "r") as file:
    file.read(5)
    print("After reading:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())


# Practice Program 8:
# Read a file in two parts using seek() and tell().
with open("data.txt", "r") as file:
    file.read(5)
    print("After first part:", file.tell())
    file.seek(10)
    print("After seek(10):", file.tell())
    print("Second part:", file.read(5))

