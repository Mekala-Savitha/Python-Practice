# ==========================================
# HYBRID INHERITANCE
# ==========================================

# Definition:
  Hybrid inheritance is a combination of two or more types
  of inheritance.
 
  It can combine single, multiple, multilevel, or hierarchical
  inheritance.

# Structure:
 
              Animal
             /      \
            ↓        ↓
         Mammal     Bird
            \        /
             \      /
              ↓    ↓
              Hybrid
 
# Syntax:

  class Parent:
      pass
 
  class Child1(Parent):
      pass

  class Child2(Parent):
      pass
 
  class Child3(Child1, Child2):
      pass


# PROGRAM 1: HYBRID INHERITANCE

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

class Cat(Animal):

    def meow(self):
        print("Cat is meowing")

class Pet(Dog, Cat):

    def play(self):
        print("Pet is playing")

pet1 = Pet()

pet1.eat()
pet1.bark()
pet1.meow()
pet1.play()


# PROGRAM 2: HYBRID INHERITANCE
# WITH CONSTRUCTORS

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class WorkingStudent(Student, Employee):

    def __init__(self, name, marks, salary):
        Student.__init__(self, name, marks)
        Employee.__init__(self, name, salary)

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Salary:", self.salary)

student1 = WorkingStudent("Savitha", 89, 30000)
student1.display()


# PROGRAM 3: DIAMOND INHERITANCE

class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        super().show()
        print("B")

class C(A):

    def show(self):
        super().show()
        print("C")

class D(B, C):

    def show(self):
        super().show()
        print("D")

obj = D()
obj.show()


# PROGRAM 4: MRO IN HYBRID INHERITANCE

class A:

    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()

print(D.mro())

