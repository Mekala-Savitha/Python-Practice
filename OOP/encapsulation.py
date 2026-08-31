# ==========================================
# ENCAPSULATION
# ==========================================

# Definition:
  Encapsulation means combining data and methods inside a class
  and controlling access to the data.

# Access levels in Python:

  Public    → variable
  Protected → _variable
  Private   → __variable


# PROGRAM 1: PUBLIC MEMBER

class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Savitha")
print("Name:", student1.name)


# PROGRAM 2: PROTECTED MEMBER

class Employee:

    def __init__(self, salary):
        self._salary = salary

employee1 = Employee(30000)
print("Salary:", employee1._salary)


# PROGRAM 3: PRIVATE MEMBER

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def display_balance(self):
        print("Balance:", self.__balance)

account1 = BankAccount(5000)
account1.display_balance()


# PROGRAM 4: GETTER AND SETTER

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

student1 = Student(80)

print("Marks:", student1.get_marks())

student1.set_marks(90)

print("Updated Marks:", student1.get_marks())


# PROGRAM 5: SETTER WITH VALIDATION

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")

account1 = BankAccount(5000)

print("Balance:", account1.get_balance())

account1.set_balance(7000)

print("Updated Balance:", account1.get_balance())

account1.set_balance(-1000)

