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


11. union()
# Returns a new set containing all unique elements.
# Syntax: set1.union(set2)
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))


12. intersection()
# Returns common elements.
# Syntax: set1.intersection(set2)
A = {1, 2, 3}
B = {2, 3, 4}
print(A.intersection(B))


13. difference()
# Returns elements present only in first set.
# Syntax: set1.difference(set2)
print(A.difference(B))


14. symmetric_difference()
# Returns elements not common to both sets.
# Syntax: set1.symmetric_difference(set2)
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))


15. intersection_update()
# Updates the set with common elements.
# Syntax: set1.intersection_update(set2)
A = {1, 2, 3}
B = {2, 3, 4}
A.intersection_update(B)
print(A)


16. difference_update()
# Removes common elements.
# Syntax: set1.difference_update(set2)
A = {1, 2, 3}
B = {2, 3, 4}
A.difference_update(B)
print(A)


17. symmetric_difference_update()
# Updates with non-common elements.
# Syntax: set1.symmetric_difference_update(set2)
A = {1, 2, 3}
B = {3, 4, 5}
A.symmetric_difference_update(B)
print(A)


18. issubset()
# Checks whether one set is a subset.
# Syntax: set1.issubset(set2)
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))


19. issuperset()
# Checks whether one set is a superset.
# Syntax: set1.issuperset(set2)
A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B))


20. isdisjoint()
# Returns True if two sets have no common elements.
# Syntax: set1.isdisjoint(set2)
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))
