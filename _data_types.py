"""
DATATYPES IN PYTHON 

Definition:
Datatypes are used to define what kind of data(value) a variable can stor.
"""

# Numeric datatype
# Numeric datatypes are used to store data in the numeric form like int,float,complex.
age=89
print(age)
print(type(age))
price=47.52
print(price)
print(type(price))
x=35+8j
print(x)
print(type(x))

# String datatype
# String datatypes are used to store one or more characters.
city="Hyderabad"
print(city)
print(type(city))
letter='S'
print(letter)
print(type(letter))


# List datatype
# List is ordered, mutable and heterogeneous collection of values.
numbers=[76,12.9,67+1j,"Rose"]
numbers[2]=5+1j
print(numbers)
print(type(numbers))

# Tuple datatype
# Tuple 8s ordered,immutable and heterogeneous collection of values.
flowers=("Rose","Lotus","Lilly")
print(type(flowers))

# Range
# Range is used to store sequence of range numbers and it is immutable.
a=range(6)

# Set datatype
# Set is an unordered, mutable and unindexed collection of unique data elements.
x={53,99.1,'C'}
print(type(x))

# Frozen set
# Frozen set is an unordered, immutable and unindexed collection of unique data elements.
a={44,89,21}
b=frozenset(a)
print(b)
print(type(b))

# Dictionary datatype
# It is an ordered collection of elements where unique keys are associated with each value.
s={"x":"456","y":"90","12.15"}
print(type(s))

# Boolean datatype
# Boolean datatype are used to store True or False value.
is_student=True
print(is_student)
print(type(is_student))
