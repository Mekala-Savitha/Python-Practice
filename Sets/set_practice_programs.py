"""

SET PRACTICE PROGRAMS

"""

# Program 1: Remove Duplicate Elements from a List
numbers = [10, 20, 20, 30, 40, 40, 50]
unique = set(numbers)
print(unique)


# Program 2: Find Union of Two Sets
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))


# Program 3: Find Intersection of Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))


# Program 4: Find Difference of Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.difference(B))


# Program 5: Find Symmetric Difference
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))


# Program 6: Check Subset
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))


# Program 7: Check Superset
A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B))


# Program 8: Check Disjoint Sets
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))


# Program 9: Add Multiple Elements to a Set
fruits = {"Apple", "Banana"}
fruits.update(["Mango", "Orange", "Grapes"])
print(fruits)


# Program 10: Remove an Element
colors = {"Red", "Green", "Blue"}
colors.remove("Green")
print(colors)


# Program 11: Find Maximum and Minimum Element
numbers = {25, 10, 45, 80, 60}
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# Program 12: Count Number of Elements
languages = {"Python", "Java", "C", "HTML"}
print("Total Elements:", len(languages))


# Program 13: Convert String to Set
text = "programming"
characters = set(text)
print(characters)


# Program 14: Find Common Characters in Two Strings
str1 = "python"
str2 = "typhoon"
common = set(str1).intersection(set(str2))
print(common)


# Program 15: Remove Duplicate Characters from a String
text = "mississippi"
result = "".join(set(text))
print(result)
