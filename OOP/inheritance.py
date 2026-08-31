# ==========================================
# INHERITANCE
# ==========================================

# Definition:
  Inheritance is an OOP feature that allows a child class
  to acquire the properties and methods of a parent class.

# Parent class → Base class / Superclass
# Child class  → Derived class / Subclass

# Syntax:

  class Parent:
      pass

  class Child(Parent):
      pass


# PROGRAM 1: BASIC INHERITANCE

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog1 = Dog()

dog1.eat()
dog1.bark()


# PROGRAM 2: INHERITING CONSTRUCTOR

class Animal:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

class Dog(Animal):
    pass

dog1 = Dog("Bruno")
dog1.display_name()


# PROGRAM 3: CHILD CLASS WITH ITS OWN METHOD

class Vehicle:

    def start(self):
        print("Vehicle is started")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")

car1 = Car()

car1.start()
car1.drive()


# PROGRAM 4: CHILD CLASS WITH ADDITIONAL DATA

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Savitha", 89)
student1.display()

