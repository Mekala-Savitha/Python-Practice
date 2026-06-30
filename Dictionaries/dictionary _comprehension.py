"""
Dictionary Comprehension

This file contains programs that demonstrate dictionary comprehension in
Python. Dictionary comprehension provides a concise and efficient way to
create dictionaries using a single line of code with optional conditions.

Programs Included

1. Basic Dictionary Comprehension
2. Squares Dictionary
3. Even Numbers Dictionary
4. Odd Numbers Dictionary
5. Dictionary with Condition

Concepts Covered

• Dictionary comprehension
• Creating dictionaries in one line
• Using range()
• Conditional dictionary comprehension
• Even and odd number filtering
• Square value generation

Learning Outcomes

After completing these programs, you will be able to:

• Create dictionaries using dictionary comprehension.
• Generate dictionaries from sequences.
• Use conditions inside dictionary comprehensions.
• Create dictionaries of squares, even numbers, and odd numbers.
• Write clean and efficient Python code.
"""

# Basic Dictionary Comprehension 
numbers=[1,2,3,4,5]
data={num:num for num in numbers}
print(data)

# Squares Dictionary 
squares={x:x*x for x in range(1,6)}
print(squares)

# Even Numbers Dictionary 
even={x:x for x in range(1,11) if x%2==0}
print(even)

# Odd Numbers Dictionary 
odd={x:x for x in range(1,10) if x%2!=0}
print(odd)

# Dictionary with Condition 
# Squares greater than 25
squares={x:x*x for x in range(1,11) if x*x>25}
print(squares)
