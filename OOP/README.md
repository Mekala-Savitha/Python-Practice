# ==========================================
# PYTHON OOP CONCEPTS
# ==========================================


# 1. CLASS
# Definition:
  A class is a blueprint or template used to create objects.

# Syntax:
  class ClassName:
     pass


# 2. OBJECT
# Definition:
  An object is an instance of a class.

# Syntax:
  object_name = ClassName()


# 3. CONSTRUCTOR
# Definition:
  A constructor is a special method that is automatically called
  when an object is created.

# Python uses __init__() as the constructor.

# Syntax:
  class ClassName:
      def __init__(self, parameters):
          self.attribute = value


# 4. INSTANCE VARIABLES
# Definition:
  Instance variables are variables that belong to a particular object.
 
# Syntax:
  self.variable = value


# 5. CLASS VARIABLES
# Definition:
  Class variables are variables shared by all objects of a class.

# Syntax:
  class ClassName:
      class_variable = value


# 6. CLASS METHOD
# Definition:
  A class method is a method that works with the class rather than
  a particular object.
 
  It uses the @classmethod decorator and cls parameter.
 
# Syntax:
  @classmethod
  def method_name(cls):
      pass


# 7. STATIC METHOD
# Definition:
  A static method is a method that does not depend on the class
  or object.
 
  It uses the @staticmethod decorator.
 
# Syntax:
  @staticmethod
  def method_name():
      pass


# 8. ENCAPSULATION
# Definition:
  Encapsulation means combining data and methods inside a class
  and controlling access to the data.
 
# Access levels:
  Public    → variable
  Protected → _variable
  Private   → __variable


# 9. GETTER
# Definition:
  A getter is a method used to access a private variable.
 
# Syntax:
  def get_variable(self):
      return self.__variable


# 10. SETTER
# Definition:
  A setter is a method used to modify a private variable.
 
# Syntax:
  def set_variable(self, value):
      self.__variable = value


# 11. INHERITANCE
# Definition:
  Inheritance allows a child class to acquire properties and
  methods from a parent class.

# Syntax:
  class Child(Parent):
      pass


# 12. TYPES OF INHERITANCE
# Definition:
  Python supports different types of inheritance:

  1. Single Inheritance
  2. Multilevel Inheritance
  3. Multiple Inheritance
  4. Hierarchical Inheritance
  5. Hybrid Inheritance


# 13. SUPER()
# Definition:
  super() is used to access methods and constructors of the
  parent class.
 
# Syntax:
  super().method_name()
 
# Constructor syntax:
  super().__init__(arguments)


# 14. METHOD OVERRIDING
# Definition:
  Method overriding occurs when a child class provides its own
  implementation of a method already defined in the parent class.
 
# Syntax:
  class Parent:
      def method(self):
          pass
 
  class Child(Parent):
      def method(self):
         pass


# 15. POLYMORPHISM
# Definition:
  Polymorphism means one interface or operation can have
  different behaviors depending on the object.
 
# Types:
  1. Method Overriding
  2. Duck Typing
  3. Function Polymorphism
  4. Operator Overloading


# 16. DUCK TYPING
# Definition:
  Duck typing means that an object's behavior is more important
  than its specific class type.
 
# Syntax:
  def function_name(object):
      object.method_name()


# 17. FUNCTION POLYMORPHISM
# Definition:
  Function polymorphism allows the same function to work with
  different types of objects.
 
# Syntax:
  def function_name(object):
      object.method_name()


# 18. OPERATOR OVERLOADING
# Definition:
  Operator overloading allows operators to perform specific
  operations on objects using special methods.
 
# Common syntax:
  def __add__(self, other):
      pass


# Common Operator Overloading Methods:

  +   → __add__()
  -   → __sub__()
  *   → __mul__()
  /   → __truediv__()
  ==  → __eq__()
  !=  → __ne__()
  >   → __gt__()
  <   → __lt__()


# 19. ABSTRACTION
# Definition:
  Abstraction means hiding unnecessary implementation details
  and showing only the essential features.
 
  Python provides abstraction using ABC and @abstractmethod.
 
# Syntax:
  from abc import ABC, abstractmethod
 
  class ClassName(ABC):
      @abstractmethod
      def method_name(self):
          pass


# ==========================================
# FOUR MAIN PRINCIPLES OF OOP
# ==========================================

# 1. Encapsulation
  Combining data and methods and controlling access to data.

# 2. Inheritance
  Acquiring properties and methods from another class.

# 3. Polymorphism
  Allowing the same operation to have different behaviors.

# 4. Abstraction
  Hiding implementation details and showing essential features.

