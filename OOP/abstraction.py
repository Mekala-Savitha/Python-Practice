# ==========================================
# ABSTRACTION
# ==========================================

# Definition:
  Abstraction means hiding implementation details and showing
  only the essential features to the user.
 
# Python provides abstraction using:
  1. ABC
  2. @abstractmethod

# Syntax:
 
  from abc import ABC, abstractmethod
 
  class ClassName(ABC):
 
      @abstractmethod
      def method_name(self):
          pass


# PROGRAM 1: BASIC ABSTRACTION

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.sound()


# PROGRAM 2: SHAPE ABSTRACTION

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle1 = Circle(5)
rectangle1 = Rectangle(10, 20)

print("Circle Area:", circle1.area())
print("Rectangle Area:", rectangle1.area())


# PROGRAM 3: PAYMENT ABSTRACTION

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")

upi1 = UPI()
card1 = Card()

upi1.pay(500)
card1.pay(1000)


# PROGRAM 4: MULTIPLE ABSTRACT METHODS

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

car1 = Car()

car1.start()
car1.stop()
