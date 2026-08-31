# ==========================================
# CLASS METHODS
# ==========================================

# Definition:
  A class method is a method that works with the class rather than
  a particular object.

# It is defined using the @classmethod decorator.
# The first parameter is cls, which refers to the class.

# Syntax:

  class ClassName:
      @classmethod
      def method_name(cls, parameters):
          pass


# PROGRAM 1: SIMPLE CLASS METHOD

class Student:

    college = "ABC College"
    @classmethod
    def display_college(cls):
        print("College:", cls.college)

Student.display_college()


# PROGRAM 2: CHANGING CLASS VARIABLE

class Student:

    college = "ABC College"
    @classmethod
    def change_college(cls, college):
        cls.college = college

print("Before:", Student.college)

Student.change_college("XYZ College")
print("After:", Student.college)


# PROGRAM 3: CLASS METHOD WITH MULTIPLE PARAMETERS

class Employee:

    company = "ABC Company"
    @classmethod
    def change_company(cls, company):
        cls.company = company

    @classmethod
    def display_company(cls):
        print("Company:", cls.company)

Employee.display_company()

Employee.change_company("XYZ Company")
Employee.display_company()


# PROGRAM 4: CLASS METHOD AS ALTERNATIVE CONSTRUCTOR

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        name, marks = data.split(",")
        return cls(name, int(marks))

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = Student.from_string("Savitha,89")
student1.display()

