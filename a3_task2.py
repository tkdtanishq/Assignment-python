# Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#     o   Square root of the number
#     o   Natural logarithm (log base e) of the number
#     o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
def sq_root(n):
    if n==0:
        return 0
    else:
        return math.sqrt(n)
def log(n):
    if n==0:
        return 0
    else:
        return math.log(n,2.71828)
def sine(n):
    if n==0:
        return 0
    else:
        return math.sin(n)

num=float(input("Enter a number: "))
if num < 0:
    print("Kindly input a positive value!!")
else:
    print(f"Square root: {sq_root(num)}\nLogarithm: {log(num)}\nSine: {sine(num)}")
