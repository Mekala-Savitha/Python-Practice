# @property in Python

## Definition

`@property` is a built-in decorator in Python used to access a method like an attribute.

It is commonly used to implement **getters and setters** and to control access to class attributes.

Properties are useful when we want to **validate or control the value** of an attribute without changing the way the attribute is accessed.

---

## Syntax

### Getter

class ClassName:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

### Getter and Setter

class ClassName:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
      

## Getter

A **getter** is used to read or retrieve the value of an attribute.

@property
def value(self):
    return self._value

Usage:

object.value

## Setter

A **setter** is used to modify or update the value of an attribute.

@value.setter
def value(self, new_value):
    self._value = new_value

Usage:

object.value = new_value


## Example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    # Getter
    @property
    def marks(self):
        return self._marks

    # Setter
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks. Enter marks between 0 and 100.")

student = Student("Savitha", 85)

print("Student Name:", student.name)
print("Marks:", student.marks)

student.marks = 95
print("Updated Marks:", student.marks)

student.marks = 120
print("Marks:", student.marks)

### Output

Student Name: Savitha
Marks: 85
Updated Marks: 95
Invalid marks. Enter marks between 0 and 100.
Marks: 95


## Key Points

* `@property` creates a **getter**.
* `@attribute.setter` creates a **setter**.
* Properties provide **controlled access** to attributes.
* Properties are useful for **validation**.
* The actual internal attribute is commonly written with `_`, such as `_marks`.
