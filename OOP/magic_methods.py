# Special / Magic Methods in Python

## Definition

Special methods, also called **magic methods** or **dunder methods**, are predefined methods in Python whose names start and end with double underscores (`__`).

They allow Python objects to work with built-in functions, operators, and language features.

Examples:

__init__()
__str__()
__len__()
__add__()
__eq__()


## General Syntax

class ClassName:

    def __special_method__(self, parameters):
        # statements

# Common Special / Magic Methods

## 1. `__init__()`

### Definition

`__init__()` is a special method that is automatically called when an object is created.

It is commonly used to initialize instance variables.

### Syntax
class ClassName:

    def __init__(self, parameters):
        self.attribute = value


## 2. `__str__()`

### Definition

`__str__()` defines the user-friendly string representation of an object.

It is automatically called when `print()` is used with an object.

### Syntax
class ClassName:

    def __str__(self):
        return "string representation"


## 3. `__repr__()`

### Definition

`__repr__()` defines the official or developer-oriented representation of an object.

It is mainly useful for debugging and development.

### Syntax
class ClassName:

    def __repr__(self):
        return "official representation"


## 4. `__len__()`

### Definition

`__len__()` defines the behavior of the built-in `len()` function when it is used with an object.

### Syntax
class ClassName:

    def __len__(self):
        return length


## 5. `__eq__()`

### Definition

`__eq__()` defines how two objects are compared using the `==` operator.

### Syntax
class ClassName:

    def __eq__(self, other):
        return self.value == other.value


## 6. `__lt__()`

### Definition

`__lt__()` defines the behavior of the less-than (`<`) operator between objects.

### Syntax
class ClassName:

    def __lt__(self, other):
        return self.value < other.value


## 7. `__gt__()`

### Definition

`__gt__()` defines the behavior of the greater-than (`>`) operator between objects.

### Syntax
class ClassName:

    def __gt__(self, other):
        return self.value > other.value


## 8. `__add__()`

### Definition

`__add__()` defines the behavior of the addition (`+`) operator between objects.

### Syntax
class ClassName:

    def __add__(self, other):
        return self.value + other.value


## 9. `__sub__()`

### Definition

`__sub__()` defines the behavior of the subtraction (`-`) operator between objects.

### Syntax
class ClassName:

    def __sub__(self, other):
        return self.value - other.value


## 10. `__mul__()`

### Definition

`__mul__()` defines the behavior of the multiplication (`*`) operator between objects.

### Syntax
class ClassName:

    def __mul__(self, other):
        return self.value * other.value


## 11. `__truediv__()`

### Definition

`__truediv__()` defines the behavior of the division (`/`) operator between objects.

### Syntax
class ClassName:

    def __truediv__(self, other):
        return self.value / other.value


## 12. `__mod__()`

### Definition

`__mod__()` defines the behavior of the modulus (`%`) operator between objects.

### Syntax
class ClassName:

    def __mod__(self, other):
        return self.value % other.value


## 13. `__contains__()`

### Definition

`__contains__()` defines the behavior of the `in` operator when checking whether a value exists in an object.

### Syntax
class ClassName:

    def __contains__(self, item):
        return item in self.data


## 14. `__call__()`

### Definition

`__call__()` allows an object to be called like a function.

### Syntax
class ClassName:

    def __call__(self, parameters):
        # statements

      
## 15. `__getitem__()`

### Definition

`__getitem__()` defines how an object responds when an item is accessed using square brackets (`[]`).

### Syntax
class ClassName:

    def __getitem__(self, index):
        return self.data[index]


## 16. `__setitem__()`

### Definition

`__setitem__()` defines how values are assigned to an object using square brackets.

### Syntax
class ClassName:

    def __setitem__(self, index, value):
        self.data[index] = value


## 17. `__delitem__()`

### Definition

`__delitem__()` defines how an item is deleted from an object using `del`.

### Syntax
class ClassName:

    def __delitem__(self, index):
        del self.data[index]


## 18. `__iter__()`

### Definition

`__iter__()` defines how an object provides an iterator.

### Syntax
class ClassName:

    def __iter__(self):
        return iter(self.data)


## 19. `__next__()`

### Definition

`__next__()` defines how the next value is obtained from an iterator.

### Syntax
class ClassName:

    def __next__(self):
        # return next value


## 20. `__enter__()`

### Definition

`__enter__()` defines the behavior when an object enters a `with` statement.

### Syntax
class ClassName:

    def __enter__(self):
        # setup
        return self


## 21. `__exit__()`

### Definition

`__exit__()` defines the behavior when an object leaves a `with` statement.

### Syntax
class ClassName:

    def __exit__(self, exc_type, exc_value, traceback):
        # cleanup

      
# Operator Mapping

| Operator / Function | Magic Method     |
| ------------------- | ---------------- |
| `+`                 | `__add__()`      |
| `-`                 | `__sub__()`      |
| `*`                 | `__mul__()`      |
| `/`                 | `__truediv__()`  |
| `%`                 | `__mod__()`      |
| `==`                | `__eq__()`       |
| `<`                 | `__lt__()`       |
| `>`                 | `__gt__()`       |
| `<=`                | `__le__()`       |
| `>=`                | `__ge__()`       |
| `!=`                | `__ne__()`       |
| `len()`             | `__len__()`      |
| `print()`           | `__str__()`      |
| `in`                | `__contains__()` |
| `[]`                | `__getitem__()`  |
| `del obj[]`         | `__delitem__()`  |
| `obj()`             | `__call__()`     |


## Example Program
      
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # __str__() -> print(object)
    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"

    # __repr__() -> repr(object)
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    # __len__() -> len(object)
    def __len__(self):
        return len(self.name)

    # __eq__() -> object1 == object2
    def __eq__(self, other):
        return self.marks == other.marks

    # __lt__() -> object1 < object2
    def __lt__(self, other):
        return self.marks < other.marks

    # __gt__() -> object1 > object2
    def __gt__(self, other):
        return self.marks > other.marks

    # __add__() -> object1 + object2
    def __add__(self, other):
        return self.marks + other.marks

    # __sub__() -> object1 - object2
    def __sub__(self, other):
        return self.marks - other.marks

    # __mul__() -> object1 * object2
    def __mul__(self, other):
        return self.marks * other.marks

    # __truediv__() -> object1 / object2
    def __truediv__(self, other):
        return self.marks / other.marks

    # __mod__() -> object1 % object2
    def __mod__(self, other):
        return self.marks % other.marks


class StudentList:
    def __init__(self, students):
        self.students = students

    # __contains__() -> item in object
    def __contains__(self, student):
        return student in self.students

    # __getitem__() -> object[index]
    def __getitem__(self, index):
        return self.students[index]

    # __setitem__() -> object[index] = value
    def __setitem__(self, index, value):
        self.students[index] = value

    # __delitem__() -> del object[index]
    def __delitem__(self, index):
        del self.students[index]

    # __iter__() -> for item in object
    def __iter__(self):
        return iter(self.students)

    # __call__() -> object()
    def __call__(self):
        return f"Total Students: {len(self.students)}"


# Creating objects
student1 = Student("Savitha", 80)
student2 = Student("Anitha", 70)

# __str__()
print(student1)

# __repr__()
print(repr(student1))

# __len__()
print("Length of name:", len(student1))

# __eq__()
print("Equal:", student1 == student2)

# __lt__()
print("Student1 < Student2:", student1 < student2)

# __gt__()
print("Student1 > Student2:", student1 > student2)

# Arithmetic magic methods
print("Addition:", student1 + student2)
print("Subtraction:", student1 - student2)
print("Multiplication:", student1 * student2)
print("Division:", student1 / student2)
print("Modulus:", student1 % student2)


# StudentList object
students = StudentList(["Savitha", "Anitha", "Rahul"])

# __contains__()
print("Savitha" in students)

# __getitem__()
print("First student:", students[0])

# __setitem__()
students[1] = "Priya"
print("After updating:", students.students)

# __delitem__()
del students[2]
print("After deleting:", students.students)

# __iter__()
print("Students:")
for student in students:
    print(student)

# __call__()
print(students())


# __enter__() and __exit__()
class FileManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with FileManager():
    print("Inside with block")


### Output

Student(Name=Savitha, Marks=80)
Student('Savitha', 80)
Length of name: 7
Equal: False
Student1 < Student2: False
Student1 > Student2: True
Addition: 150
Subtraction: 10
Multiplication: 5600
Division: 1.1428571428571428
Modulus: 10
True
First student: Savitha
After updating: ['Savitha', 'Priya', 'Rahul']
After deleting: ['Savitha', 'Priya']
Students:
Savitha
Priya
Total Students: 2
Entering context
Inside with block
Exiting context


### Magic Methods Covered

| Magic Method     | Demonstrated          |
| ---------------- | --------------------- |
| `__init__()`     | Object initialization |
| `__str__()`      | `print()`             |
| `__repr__()`     | `repr()`              |
| `__len__()`      | `len()`               |
| `__eq__()`       | `==`                  |
| `__lt__()`       | `<`                   |
| `__gt__()`       | `>`                   |
| `__add__()`      | `+`                   |
| `__sub__()`      | `-`                   |
| `__mul__()`      | `*`                   |
| `__truediv__()`  | `/`                   |
| `__mod__()`      | `%`                   |
| `__contains__()` | `in`                  |
| `__getitem__()`  | `[]`                  |
| `__setitem__()`  | `[]= `                |
| `__delitem__()`  | `del`                 |
| `__iter__()`     | `for` loop            |
| `__call__()`     | `object()`            |
| `__enter__()`    | `with`                |
| `__exit__()`     | `with`                |

      

# Key Points

* Special methods begin and end with double underscores.
* They are also called **magic methods** or **dunder methods**.
* Python automatically calls many special methods when the corresponding operation is performed.
* They allow custom objects to work with Python's built-in functions and operators.
* `__init__()` initializes objects.
* `__str__()` controls the readable string representation.
* `__repr__()` provides a developer-oriented representation.
* Operator methods allow objects to support operations such as `+`, `-`, `*`, and comparisons.
* `__call__()` makes an object callable like a function.
* `__getitem__()` and related methods allow custom objects to behave like containers.
