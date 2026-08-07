"""
RECURSION IN PYTHON

Definition:
Recursion is a process in which a function calls itself
until a specified stopping condition (base case) is reached.

Syntax:

def function_name(parameters):
    if base_condition:
        return
    function_name(parameters)
"""

# Example 1: Print 1 to 5
def display(n):
    if n>5:
        return
    print(n)
    display(n+1)
display(1)

# Example 2: Print 5 to 1
def reverse(n):
    if n==0:
        return
    print(n)
    reverse(n-1)
reverse(5)

# Example 3: Factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

# Example 4: Sum of First N Numbers
def total(n):
    if n==0:
        return 0
    return n+total(n-1)
print(total(5))

# Example 5: Fibonacci
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

# Example 6: Power of a Number
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(2,5))

# Example 7: Count Digits
def count(n):
    if n<10:
        return 1
    return 1+count(n//10)
print(count(12345))

# Example 8: Reverse a String
def reverse_string(text):
    if len(text)==0:
        return text
    return reverse_string(text[1:])+text[0]
print(reverse_string("Python"))

# Example 9: Sum of Digits
def digit_sum(n):
    if n==0:
        return 0
    return n%10+digit_sum(n//10)
print(digit_sum(1234))

# Example 10: Print Alphabet Recursively
def alphabet(ch):
    if ch>'E':
        return
    print(ch)
    alphabet(chr(ord(ch)+1))
alphabet('A')
