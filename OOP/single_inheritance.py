# ==========================================
# SINGLE INHERITANCE
# ==========================================

# Definition:
  Single inheritance occurs when one child class inherits
  from one parent class.

# Structure:
 
  Parent
    ↓
  Child
 
# Syntax:

  class Parent:
      pass
 
  class Child(Parent):
      pass


# PROGRAM 1: BASIC SINGLE INHERITANCE

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog1 = Dog()

dog1.eat()
dog1.bark()


# PROGRAM 2: SINGLE INHERITANCE WITH CONSTRUCTOR

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Marks:", self.marks)

student1 = Student("Savitha", 89)

student1.display_name()
student1.display()


# PROGRAM 3: CHILD CLASS ADDING A METHOD

class Vehicle:

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")

car1 = Car()

car1.start()
car1.drive()


# PROGRAM 4: METHOD OVERRIDING IN SINGLE INHERITANCE

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.sound()

