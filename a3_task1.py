# #Write a python program that:
#   1. Defines a function named factorial that takes a number as an argument and calculates  its factorial using a loop or recursion.
#   2. Returns the calculated factorial.
#   3. Calls the function with a sample number and prints the output.

def factorial(num): #defining a function
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1) #recursive function

n=int(input("Enter a number: "))
print(f"Factorial of {n} is: {factorial(n)}")