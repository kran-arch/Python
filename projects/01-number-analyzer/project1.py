#Project-1: Simply to learn how to use Python
#I'll be using these small projects to learn how to use Python and its syntax.
#As well as to put real-world problems into code and solve them using Python.
#Ill also be using these projects to learn how to use GitHub and version control.
#Ill uplaod these projects to GitHub and use them as a portfolio to showcase my skills and knowledge in Python.

num = int(input("Enter a number: "))
print(num)

if num > 0:
    print("Type: Positive")
elif num < 0:
    print("Type: Negative")
else:
    print("Type: Zero")

if num % 2 == 0:
    print("parity: Even")
else:
    print("parity: Odd")


if num % 5 == 0:
    print("Divisible by 5: Yes")
else:
    print("Divisible by 5: No")

absolute_value = abs(num)
print(f"absolute_value: {absolute_value}")

square = num ** 2
print(f"square: {square}")

cube = num ** 3
print(f"cube: {cube}")