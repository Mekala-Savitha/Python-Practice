# ==========================================
# HIERARCHICAL INHERITANCE
# ==========================================

# Definition:
  Hierarchical inheritance occurs when multiple child classes
  inherit from the same parent class.
 
# Structure:
 
              Parent
             /      \
            ↓        ↓
         Child1    Child2
 
# Syntax:

  class Parent:
      pass
 
  class Child1(Parent):
      pass
 
  class Child2(Parent):
      pass


# PROGRAM 1: BASIC HIERARCHICAL INHERITANCE

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

class Cat(Animal):

    def meow(self):
        print("Cat is meowing")

dog1 = Dog()

dog1.eat()
dog1.bark()

cat1 = Cat()

cat1.eat()
cat1.meow()


# PROGRAM 2: HIERARCHICAL INHERITANCE
# WITH DIFFERENT METHODS

class Person:

    def introduce(self):
        print("I am a person")

class Student(Person):

    def study(self):
        print("Student is studying")

class Teacher(Person):

    def teach(self):
        print("Teacher is teaching")

student1 = Student()

student1.introduce()
student1.study()

teacher1 = Teacher()

teacher1.introduce()
teacher1.teach()


# PROGRAM 3: HIERARCHICAL INHERITANCE
# WITH CONSTRUCTOR

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
        self.display_name()
        print("Marks:", self.marks)

class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        self.display_name()
        print("Subject:", self.subject)

student1 = Student("Savitha", 89)
student1.display()

teacher1 = Teacher("Nivrithi", "Python")
teacher1.display()


# PROGRAM 4: HIERARCHICAL INHERITANCE
# WITH METHOD OVERRIDING

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

dog1 = Dog()
dog1.sound()

cat1 = Cat()
cat1.sound()
