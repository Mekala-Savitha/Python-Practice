# ==========================================
# INSTANCE VARIABLES AND CLASS VARIABLES
# ==========================================

  INSTANCE VARIABLES
# Definition:
  Instance variables are variables that belong to a particular object.
  They are usually defined inside the __init__() method using self.

# Syntax:
  class ClassName:
      def __init__(self):
          self.variable = value


  CLASS VARIABLES
# Definition:
  Class variables are variables that belong to the class and are
  shared by all objects of that class.

# Syntax:
  class ClassName:
      class_variable = value


# PROGRAM 1: INSTANCE VARIABLES

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Savitha", 89)
student2 = Student("Nivrithi", 92)

student1.display()
student2.display()


# PROGRAM 2: CLASS VARIABLE

class Student:

    college = "ABC College"
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college)

student1 = Student("Savitha")
student2 = Student("Nivrithi")

student1.display()
student2.display()


# PROGRAM 3: INSTANCE + CLASS VARIABLES

class Employee:

    company = "ABC Company"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

employee1 = Employee("Savitha", 30000)
employee2 = Employee("Nivrithi", 35000)

employee1.display()
employee2.display()


# PROGRAM 4: CHANGING CLASS VARIABLE

class Car:

    company = "Toyota"
    def __init__(self, model):
        self.model = model

    def display(self):
        print("Model:", self.model)
        print("Company:", Car.company)

car1 = Car("Camry")
car2 = Car("Corolla")

Car.company = "Honda"
car1.display()
car2.display()
