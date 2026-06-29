# Tuple Constructor

# The tuple() constructor is used to create a tuple from iterable objects such as lists, strings, sets, and ranges.
# It can also be used to create an empty tuple.
# This section demonstrates how the tuple() constructor converts different iterable data types into tuples and compares tuple creation using the tuple() constructor and tuple literals ().

# Create an Empty Tuple using tuple()
t=tuple()
print(t)

# Create a Tuple from a List
numbers=[12,27,42,57]
t=tuple(numbers)
print(t)

# Create a Tuple from String
text="savitha"
t=tuple(text)
print(t)

# Create a Tuple from a Set
numbers={5,8,1,7}
t=tuple(numbers)
print(t)

# Create a Tuple from a range() object
t=tuple(range(1,6))
print(t)

# Compare () and tuple()
t1=(10,23,37)
t2=tuple([10,23,37])
print("Using():",t1)
print("Using tuple():",t2)
