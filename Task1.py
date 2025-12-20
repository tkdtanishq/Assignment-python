#WAP that does the following:
#   a.Takes two numbers as input from the user.
#   b.Performs the basic mathematical operations on these two numbers
#   c.Display the results of each operation on the screen.

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
print("Result:\nAddition:",add,"\nSubtraction:",sub,"\nMultiplication:",mul,"\nDivision:",round(div,2))
print("Some other mathematical operations:")
fdiv=a//b
mod=a%b
print("Floor Division:",fdiv,"\nModulos:",mod)