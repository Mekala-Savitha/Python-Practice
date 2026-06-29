# Tuple Slicing
# Tuple slicing is used to access a specific range of elements from a tuple.
# It allows you to retrieve a portion of a tuple by specifying the start index, stop index, and optional step value. Since tuples are immutable, slicing creates a new tuple without modifying the original one.
# This section demonstrates different slicing techniques for accessing, skipping, and reversing tuple elements.

data=(19,"savitha",39.6,'R',45,172)
# Slice using start and stop indexes
print(data[0:5])
# Slice from beginning to index 4
print(data[:4])
# Slice from index 1 to the end
print(data[1:])
# Slice using step value
print(data[0:4:2])
# Print alternate elements 
print(data[::2])
# Reverse the tuple
print(data[::-1])
# Print first three elements 
print(data[:3])
# Print last three elements 
print(data[-3:])
# Extract middle elements 
print(data[1:4])
# Create a new tuple using slicing 
new_tuple=data[1:5]
print(new_tuple)
