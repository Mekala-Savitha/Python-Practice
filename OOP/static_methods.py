# ==========================================
# STATIC METHODS
# ==========================================

# Definition:
  A static method is a method that does not depend on the object
  or class.

# It is defined using the @staticmethod decorator.
# It does not require self or cls.
 
# Syntax:

  class ClassName:
      @staticmethod
      def method_name(parameters):
          pass


# PROGRAM 1: SIMPLE STATIC METHOD

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

result = Calculator.add(10, 20)
print("Sum:", result)


# PROGRAM 2: STATIC METHOD WITH CONDITION

class Number:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

print("Is Even:", Number.is_even(20))


# PROGRAM 3: MULTIPLE STATIC METHODS

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def subtract(a, b):
        return a - b

print("Addition:", Calculator.add(10, 5))
print("Multiplication:", Calculator.multiply(10, 5))
print("Subtraction:", Calculator.subtract(10, 5))


# PROGRAM 4: STATIC METHOD IN A CLASS

class Student:

    def __init__(self, name):
        self.name = name
    @staticmethod
    def welcome():
        print("Welcome to Python OOP")

    def display(self):
        print("Name:", self.name)

student1 = Student("Savitha")

student1.display()
Student.welcome()

