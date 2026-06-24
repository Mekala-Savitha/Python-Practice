"""
MODULES IN PYTHON

Definition:
A module is a file which contains functions,classes and variables.

Syntax for importing a Module:
import module_name
Modules are 2 types:
1.Buit_in_modules
2.User_defined_modules

1.Built_in_modules:
The modules which are already developed are called as "Buit_in_modules".
"""

# String Module
a="NIVRITHI"
b="."
c="rithanya"
print(b.join(a))
print(len(a))
print(a.lower())
print(c.upper())

# Math Module 
import math
print(math.sqrt(25))
print(math.pow(5,2))
print(math.factorial(4))
print(math.pi)

# Statistics Module
import statistics 
x=[2,7,1,5]
print(statistics.mean(x))
print(statistics.median(x))
print(statistics.mode(x))

# Random Module
import random
student=["Nivrithi","Rithanya","Savitha","Radhika"]
print(random.choice(student))
print(random.random)
print(random.randit(1,15))

# Datetime Module
from datetime import datetime
now=datetime.now()
print(now)

# OS Module
import os
print(os.getcwd())

# Sys Module
import sys
print(sys.version)
print("Program is getting closed")
print(sys.exit())
