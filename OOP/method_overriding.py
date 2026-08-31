# ==========================================
# METHOD OVERRIDING
# ==========================================

# Definition:
  Method overriding occurs when a child class provides its own
  implementation of a method that is already defined in the
  parent class.
 
# Syntax:
 
  class Parent:
      def method(self):
          pass
 
  class Child(Parent):
      def method(self):
          pass


# PROGRAM 1: BASIC METHOD OVERRIDING

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.sound()


# PROGRAM 2: METHOD OVERRIDING WITH MULTIPLE CHILD CLASSES

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


# PROGRAM 3: METHOD OVERRIDING WITH CONSTRUCTORS

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

student1 = Student("Savitha", 89)
student1.display()

teacher1 = Teacher("Nivrithi", "Python")
teacher1.display()


# PROGRAM 4: METHOD OVERRIDING WITH super()

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog1 = Dog()
dog1.sound()
