"""
REDUCE FUNCTION IN PYTHON

Definition:
The reduce() function applies a function cumulatively to the
elements of an iterable and returns a single value.

Syntax:

from functools import reduce

reduce(function, iterable)
"""

from functools import reduce

# Example 1: Sum of Numbers
numbers = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,numbers))

# Example 2: Product of Numbers
numbers = [2,3,4]
print(reduce(lambda x,y:x*y,numbers))

# Example 3: Find Maximum
numbers = [10,30,20,50]
print(reduce(lambda x,y:x if x>y else y,numbers))

# Example 4: Find Minimum
numbers = [10,30,20,50]
print(reduce(lambda x,y:x if x<y else y,numbers))

# Example 5: Sum of Even Numbers
numbers = [2,4,6,8]
print(reduce(lambda x,y:x+y,numbers))

# Example 6: Concatenate Strings
words = ["Python","Full","Stack"]
print(reduce(lambda x,y:x+" "+y,words))

# Example 7: Largest String
words = ["apple","banana","kiwi"]
print(reduce(lambda x,y:x if len(x)>len(y) else y,words))

# Example 8: Multiply List by 10
numbers = [10,20]
print(reduce(lambda x,y:(x+y)*10,numbers))

# Example 9: Sum of Marks
marks = [80,90,70,85]
print(reduce(lambda x,y:x+y,marks))

# Example 10: Difference of Numbers
numbers = [100,20,10]
print(reduce(lambda x,y:x-y,numbers))
