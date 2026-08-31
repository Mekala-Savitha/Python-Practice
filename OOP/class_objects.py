# ==========================================
# CLASSES AND OBJECTS
# ==========================================

  CLASS
# Definition:
  A class is a blueprint or template used to create objects.

# Syntax:
  class ClassName:
      pass


  OBJECT
# Definition:
  An object is an instance of a class.

# Syntax:
  object_name = ClassName()


# PROGRAM 1: SIMPLE CLASS AND OBJECT

class Student:
    def display(self):
        print("Student is studying")

student1 = Student()
student1.display()


# PROGRAM 2: STUDENT CLASS

class Student:
    def display(self):
        print("Name: Savitha")
        print("Marks: 89")

student1 = Student()
student1.display()


# PROGRAM 3: CAR CLASS

class Car:
    def start(self):
        print("Car is starting")

    def drive(self):
        print("Car is driving")

car1 = Car()
car1.start()
car1.drive()


# PROGRAM 4: PERSON CLASS

class Person:
    def introduce(self):
        print("I am a person")

person1 = Person()
person1.introduce()

