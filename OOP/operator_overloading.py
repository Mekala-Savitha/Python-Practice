# ==========================================
# OPERATOR OVERLOADING
# ==========================================

  Operator overloading allows operators to work with objects
  using special methods (dunder methods).

# +   -> __add__()
# -   -> __sub__()
# *   -> __mul__()
# /   -> __truediv__()
# ==  -> __eq__()
# !=  -> __ne__()
# >   -> __gt__()
# <   -> __lt__()


class Number:

    def __init__(self, value):
        self.value = value

    # Addition
    def __add__(self, other):
        return Number(self.value + other.value)

    # Subtraction
    def __sub__(self, other):
        return Number(self.value - other.value)

    # Multiplication
    def __mul__(self, other):
        return Number(self.value * other.value)

    # Division
    def __truediv__(self, other):
        return Number(self.value / other.value)

    # Equal
    def __eq__(self, other):
        return self.value == other.value

    # Not Equal
    def __ne__(self, other):
        return self.value != other.value

    # Greater Than
    def __gt__(self, other):
        return self.value > other.value

    # Less Than
    def __lt__(self, other):
        return self.value < other.value

num1 = Number(50)
num2 = Number(10)

# Arithmetic Operators

result = num1 + num2
print("Addition:", result.value)

result = num1 - num2
print("Subtraction:", result.value)

result = num1 * num2
print("Multiplication:", result.value)

result = num1 / num2
print("Division:", result.value)

# Comparison Operators

print("Equal:", num1 == num2)
print("Not Equal:", num1 != num2)
print("Greater:", num1 > num2)
print("Less:", num1 < num2)
