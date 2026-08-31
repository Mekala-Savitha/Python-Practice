# ==========================================
# MULTILEVEL INHERITANCE
# ==========================================

# Definition:
  Multilevel inheritance occurs when a class inherits from another
  class, which itself inherits from another class.
 
# Structure:
 
  Grandparent
       ↓
     Parent
       ↓
      Child
 
# Syntax:
 
  class Grandparent:
      pass

  class Parent(Grandparent):
      pass

  class Child(Parent):
      pass


# PROGRAM 1: BASIC MULTILEVEL INHERITANCE

class Animal:

    def eat(self):
        print("Animal is eating")

class Mammal(Animal):

    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):

    def bark(self):
        print("Dog is barking")

dog1 = Dog()

dog1.eat()
dog1.walk()
dog1.bark()


# PROGRAM 2: MULTILEVEL INHERITANCE WITH CONSTRUCTORS

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class CollegeStudent(Student):

    def __init__(self, name, marks, college):
        super().__init__(name, marks)
        self.college = college

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", self.college)

student1 = CollegeStudent("Savitha", 89, "ABC College")
student1.display()


# PROGRAM 3: MULTILEVEL INHERITANCE WITH METHODS

class Person:

    def introduce(self):
        print("I am a person")

class Student(Person):

    def study(self):
        print("I am studying")

class CollegeStudent(Student):

    def attend_class(self):
        print("I am attending college class")

student1 = CollegeStudent()

student1.introduce()
student1.study()
student1.attend_class()


# PROGRAM 4: METHOD OVERRIDING IN MULTILEVEL

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
