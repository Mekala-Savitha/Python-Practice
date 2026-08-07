"""
FUNCTION PRACTICE PROGRAMS
"""

# Program 1: Addition of Two Numbers
def add(a, b):
    return a + b
print(add(10, 20))


# Program 2: Subtraction of Two Numbers
def subtract(a, b):
    return a - b
print(subtract(20, 10))


# Program 3: Multiplication of Two Numbers
def multiply(a, b):
    return a * b
print(multiply(5, 6))


# Program 4: Division of Two Numbers
def divide(a, b):
    return a / b
print(divide(20, 5))


# Program 5: Find Maximum of Three Numbers
def maximum(a, b, c):
    return max(a, b, c)
print(maximum(10, 30, 20))


# Program 6: Check Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(even_odd(25))


# Program 7: Check Prime Number
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(17))


# Program 8: Find Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))


# Program 9: Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)
print()


# Program 10: Reverse a String
def reverse(text):
    return text[::-1]
print(reverse("Python"))


# Program 11: Check Palindrome
def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    return "Not Palindrome"
print(palindrome("madam"))


# Program 12: Count Vowels
def vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
print(vowels("Python Programming"))


# Program 13: Find Sum of List Elements
def total(numbers):
    return sum(numbers)
print(total([10, 20, 30, 40]))


# Program 14: Find Largest Element in a List
def largest(numbers):
    return max(numbers)
print(largest([25, 80, 45, 90, 60]))


# Program 15: Student Grade
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"
print(grade(88))
