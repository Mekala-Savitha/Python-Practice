# Tuple Indexing

# This section demonstrates how to access elements in a tuple using positive and negative indexing.
# Positive indexing starts from 0 and moves from left to right, while negative indexing starts from -1 and moves from right to left.
# The example programs show how to retrieve specific elements using both indexing methods, helping you understand how tuples are accessed efficiently in Python.

# Positive indexing 
t=(10,21,45,67)
print("First element:",t[0])
print("Second element:",t[1])
print("Third element:",t[2])
print("Fourth element:",t[3])

# Negative indexing 
t=(11,25,46,77)
print(t[-1])
print(t[-2])
print(t[-3])
print(t[-4])

# Printing all elements using positive indexing 
numbers=(10,23,37,42,58)
for i in range(len(numbers)):
    print(numbers[i])

# Printing all elements using negative indexing 
numbers=(10,23,37,42,58)
for i in range(1,len(numbers)+1):
    print(numbers[-i])
