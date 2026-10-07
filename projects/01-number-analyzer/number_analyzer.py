#An advanced version of project1.py with functions and a loop to allow the user to enter multiple numbers and get their properties.
#This helped me learn how to use functions and loops in Python and also how to handle user input and errors.


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def check_parity(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_divisible_by_5(num):
    if num % 5 == 0:
        return "Yes"
    else:
        return "No"

def calculate_absolute_value(num):
    return abs(num)

def calculate_square(num):
    return num ** 2

def calculate_cube(num):
    return num ** 3
 

while True: 

 user_input = input("Enter a number or 'q' to quit: ")
 
 if user_input == 'q':
    print("Goodbye!")
    break
 
 try:
    num = int(user_input)
 except ValueError:
    print("Invalid input. Please enter a valid integer or 'q' to quit.")
    continue
 
 num = int(user_input)   

 print(f"Number: {num}")
 print(f"Type: {check_number(num)}")
 print(f"Parity: {check_parity(num)}")
 print(f"Divisible by 5: {is_divisible_by_5(num)}")
 print(f"Absolute Value: {calculate_absolute_value(num)}")
 print(f"Square: {calculate_square(num)}")
 print(f"Cube: {calculate_cube(num)}")