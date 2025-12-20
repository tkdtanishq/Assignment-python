#WAP that does the following:
#   a) Takes two numbers as input from the user.
#   b) Performs the basic mathematical operation on these numbers.
#   c) Displays the result of each operation on the screen.
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
add=a+b
sub=a-b
mult=a*b
div=a/b
fldiv=a//b
mod=a%b
print("Addition:",add,"\nSubtraction:",sub,"\nMultiplication:",mult,"\nDivision:",div)
print("\n \nSOME EXTRAS \nFloor Division:",fldiv,"\nModulus:",mod)