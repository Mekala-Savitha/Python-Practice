"""
PYTHON SET OPERATORS

Definition:
Set operators are used to perform mathematical operations
between two or more sets.

Operators:
1. Union (|)
2. Intersection (&)
3. Difference (-)
4. Symmetric Difference (^)
5. Membership (in)
6. Membership (not in)
"""


1. Union Operator (|)
# Combines all unique elements from both sets.
# Syntax: set1 | set2
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)


2. Intersection Operator (&)
# Returns common elements from both sets.
# Syntax: set1 & set2
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)


3. Difference Operator (-)
# Returns elements present in the first set
# but not in the second set.
# Syntax: set1 - set2
A = {1, 2, 3}
B = {2, 3, 4}
print(A - B)
print(B - A)


4. Symmetric Difference Operator (^)
# Returns elements present in either set,
# but not in both.
# Syntax: set1 ^ set2
A = {1, 2, 3}
B = {3, 4, 5}
print(A ^ B)


5. Membership Operator (in)
# Checks whether an element exists in a set.
# Syntax: element in set_name
numbers = {10, 20, 30, 40}
print(20 in numbers)
print(50 in numbers)


6. Membership Operator (not in)
# Checks whether an element does not exist in a set.
# Syntax: element not in set_name
numbers = {10, 20, 30, 40}
print(50 not in numbers)
print(20 not in numbers)
