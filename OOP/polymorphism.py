# ==========================================
# POLYMORPHISM
# ==========================================

# Definition:
  Polymorphism means "many forms".
  It allows the same method, function, or operation to behave
  differently depending on the object.


# PROGRAM 1: METHOD OVERRIDING

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


# PROGRAM 2: DUCK TYPING

class Dog:

    def sound(self):
        print("Dog barks")

class Cat:

    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

dog1 = Dog()
cat1 = Cat()

make_sound(dog1)
make_sound(cat1)


# PROGRAM 3: FUNCTION POLYMORPHISM

class Student:

    def display(self):
        print("Student is studying")

class Teacher:

    def display(self):
        print("Teacher is teaching")

def show(person):
    person.display()

student1 = Student()
teacher1 = Teacher()

show(student1)
show(teacher1)


# PROGRAM 4: POLYMORPHISM WITH DIFFERENT OBJECTS

class Circle:

    def area(self):
        return 3.14 * 5 * 5

class Rectangle:

    def area(self):
        return 10 * 20

class Square:

    def area(self):
        return 8 * 8

def calculate_area(shape):
    print("Area:", shape.area())

circle1 = Circle()
rectangle1 = Rectangle()
square1 = Square()

calculate_area(circle1)
calculate_area(rectangle1)
calculate_area(square1)
