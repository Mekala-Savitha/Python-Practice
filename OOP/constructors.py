# ==========================================
# CONSTRUCTORS
# ==========================================

# Definition:
  A constructor is a special method that is automatically called
  when an object is created.

  In Python, __init__() is commonly used as a constructor.

# Syntax:
  class ClassName:
      def __init__(self, parameters):
          self.attribute = value


# PROGRAM 1: SIMPLE CONSTRUCTOR

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

student1 = Student("Savitha")
student1.display()


# PROGRAM 2: CONSTRUCTOR WITH MULTIPLE PARAMETERS

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

student1 = Student("Savitha", 23, 89)
student1.display()


# PROGRAM 3: CONSTRUCTOR IN BANK ACCOUNT

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

account1 = BankAccount(101, 5000)
account1.display()


# PROGRAM 4: CONSTRUCTOR WITH DEFAULT VALUE

class Employee:

    def __init__(self, name, salary=25000):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Savitha")
employee1.display()

employee2 = Employee("Nivrithi", 30000)
employee2.display()

