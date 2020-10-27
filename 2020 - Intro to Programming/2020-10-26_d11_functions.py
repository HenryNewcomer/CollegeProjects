##########################
# Author: Henry Newcomer
##########################

############
# Question 1
############

def f():
    pass # Does nothing.

############
# Question 2
############

def ping():
    return "Ping!"

print(ping())

############
# Question 3
############


# This looks like less work, but it's harder to understand what's even
# going on. Try to be descriptive with the names of variables, functions, etc.
from math import pi
def v(r): return (4.0/3.0)*pi*r**3
print(v(20)) # Should output ~33,510.32

############
# Question 4
############

# This is way easier to read...
def areaOfTriangle(base = 0, height = 0):
    area = (base * height) / 2
    return area

print(areaOfTriangle(20,20)) # Should output 200

############
# Question 5
############

def convertToCm(feet = 0, inches = 0):
    totalInches = feet * 12 + inches
    totalCm = totalInches * 2.54
    return totalCm

print(f"{convertToCm(5, 11)}cm") # Should output ~180.339cm

############
# Question 6
############

def g(requiredParam, aKeyword = 0):
    return float(requiredParam) + aKeyword

print(g(5, aKeyword = 4)) # Should print 9
# g(5, 4) would also work in this case.
