# ==========================================
# MULTIPLE INHERITANCE
# ==========================================

# Definition:
  Multiple inheritance occurs when one child class inherits
  from two or more parent classes.
 
# Structure:
 
  Parent1       Parent2
      \           /
       \         /
         Child
 
# Syntax:
 
  class Child(Parent1, Parent2):
      pass


# PROGRAM 1: BASIC MULTIPLE INHERITANCE

class Father:

    def driving(self):
        print("Father can drive")

class Mother:

    def cooking(self):
        print("Mother can cook")

class Child(Father, Mother):

    def playing(self):
        print("Child can play")

child1 = Child()

child1.driving()
child1.cooking()
child1.playing()


# PROGRAM 2: MULTIPLE INHERITANCE WITH CONSTRUCTORS

class Father:

    def __init__(self, father_name):
        self.father_name = father_name

class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name

class Child(Father, Mother):

    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def display(self):
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)

child1 = Child("Ramulu", "Posani")
child1.display()


# PROGRAM 3: METHOD NAME CONFLICT

class Father:

    def show(self):
        print("Father's method")

class Mother:

    def show(self):
        print("Mother's method")

class Child(Father, Mother):
    pass

child1 = Child()
child1.show()


# PROGRAM 4: METHOD RESOLUTION ORDER (MRO)

class Father:

    def show(self):
        print("Father's method")
        super().show()

class Mother:

    def show(self):
        print("Mother's method")
        super().show()

class Child(Father, Mother):

    def show(self):
        super().show()
        print("Child's method")

child1 = Child()
child1.show()


# MRO determines the order in which Python searches for methods.
# Check MRO using:

  print(Child.mro())

# or:

  print(Child.__mro__)
