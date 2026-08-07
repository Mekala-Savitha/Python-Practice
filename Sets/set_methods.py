"""
PYTHON SET METHODS

Definition:
Set methods are built-in functions used to perform
operations such as adding, removing, copying, and
updating elements in a set.
"""

1. add()
# Adds a single element to the set.
# Syntax: set_name.add(element)
fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)


2. update()
# Adds multiple elements to the set.
# Syntax: set_name.update(iterable)
numbers = {10, 20}
numbers.update([30, 40, 50])
print(numbers)


3. remove()
# Removes the specified element.
# Raises KeyError if the element is not found.
# Syntax: set_name.remove(element)
colors = {"Red", "Green", "Blue"}
colors.remove("Green")
print(colors)


4. discard()
# Removes the specified element.
# Does not raise an error if the element is not found.
# Syntax: set_name.discard(element)
animals = {"Dog", "Cat", "Cow"}
animals.discard("Lion")
print(animals)


5. pop()
# Removes and returns a random element.
# Syntax: set_name.pop()
letters = {"A", "B", "C"}
print(letters.pop())
print(letters)


6. clear()
# Removes all elements from the set.
# Syntax: set_name.clear()
data = {1, 2, 3, 4}
data.clear()
print(data)


7. copy()
# Returns a shallow copy of the set.
# Syntax: new_set = set_name.copy()
original = {"Python", "Java", "C"}
copied = original.copy()
print("Original:", original)
print("Copied:", copied)


8. len()
# Returns the number of elements.
# Syntax: len(set_name)
numbers = {10, 20, 30, 40}
print(len(numbers))


9. max()
# Returns the largest element.
# Syntax: max(set_name)
numbers = {15, 30, 45, 10}
print(max(numbers))


10. min()
# Returns the smallest element.
# Syntax: min(set_name)
numbers = {15, 30, 45, 10}
print(min(numbers))
