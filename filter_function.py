"""
FILTER FUNCTION IN PYTHON

Definition:
The filter() function selects only those elements from an
iterable that satisfy a specified condition.

Syntax:
filter(function, iterable)
"""

# Example 1: Even Numbers
numbers = [1,2,3,4,5,6,7,8]
result = filter(lambda x:x%2==0,numbers)
print(list(result))

# Example 2: Odd Numbers
numbers = [1,2,3,4,5,6]
result = filter(lambda x:x%2!=0,numbers)
print(list(result))

# Example 3: Numbers Greater Than 20
numbers = [10,20,30,40,50]
result = filter(lambda x:x>20,numbers)
print(list(result))

# Example 4: Positive Numbers
numbers = [-5,-2,0,4,7]
result = filter(lambda x:x>0,numbers)
print(list(result))

# Example 5: Strings Longer Than 5 Characters
words = ["apple","banana","cat","python"]
result = filter(lambda x:len(x)>5,words)
print(list(result))

# Example 6: Names Starting with 'A'
names = ["Anu","Ravi","Asha","Kiran"]
result = filter(lambda x:x.startswith("A"),names)
print(list(result))

# Example 7: Multiples of 3
numbers = [3,5,6,9,10,12]
result = filter(lambda x:x%3==0,numbers)
print(list(result))

# Example 8: Marks Greater Than or Equal to 35
marks = [20,35,50,10,90]
result = filter(lambda x:x>=35,marks)
print(list(result))

# Example 9: Vowels
letters = ['a','b','e','f','i','o']
result = filter(lambda x:x in "aeiou",letters)
print(list(result))

# Example 10: Numbers Less Than 100
numbers = [50,120,80,150,90]
result = filter(lambda x:x<100,numbers)
print(list(result))
