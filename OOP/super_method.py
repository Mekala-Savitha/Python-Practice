# ==========================================
# SUPER() METHOD
# ==========================================

# Definition:
  super() is used to access methods and constructors
  of the parent class.
 
# Syntax:
 
  super().method_name()
 
  Constructor:
 
  super().__init__(arguments)


# PROGRAM 1: SUPER() WITH CONSTRUCTOR

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


# PROGRAM 2: SUPER() WITH METHOD

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog1 = Dog()
dog1.sound()


# PROGRAM 3: SUPER() WITH CONSTRUCTOR AND METHOD

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        super().display()
        print("Model:", self.model)

car1 = Car("Toyota", "Camry")
car1.display()


# PROGRAM 4: SUPER() IN MULTILEVEL INHERITANCE

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):

    def sound(self):
        super().sound()
        print("Mammal makes a sound")

class Dog(Mammal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog1 = Dog()
dog1.sound()
