#This is the simple number guessing game, where the user has to guess a number between 1 and 100. The user has 10 attempts to guess the number. 
#If the user guesses the number correctly, they win. If they run out of attempts, they lose. The user can also quit the game at any time by entering 'q'.
# This project helped me practice loops, conditionals, user input,
# exception handling, and basic program flow in Python.
# Learned how to use import statements to use Python modules.
# This project contains many small bugs that I had to fix, 
# which helped me learn how to debug my code and improve my problem-solving skills.
# The upgraded version of this project will include different structures, such as functions, to make the code more organized and easier to read.
# I am leaving this project here for now, and working on the upgraded version of this project.

import random

secret_number = random.randint(1, 100)
print(f"The secret number is: {secret_number}") #For debugging purposes, this line can be removedin the final version of the game.

print("Welcome to the Number Guessing Game!")
print("I have selected a secret number between 1 and 100. Try to guess it!")
print("Guess the number and I will tell you if it's too high, too low, or correct.")
print("you only have 10 attempts to guess the number, so choose wisely!")
print("Let's begin!")

attempts = 0

while True:

 guess_str = input("Enter your guess | enter q to quit: ")
 
 if guess_str == "q":
    break

 try:
    guess = int(guess_str)
 except ValueError:
    print("Please enter a valid number.")
    continue
 
 attempts+=1

 
 if guess == secret_number:
     print("Correct!")
     break

 if attempts >= 10:
     print("Hah!, you've reached the maximum number of attempts. Game over!")
     break
 
 
 if guess < secret_number:
     print("Too low!")
 else:
     print("Too high!")


if guess_str == "q":
    print("come back soon!")
else:
    print(f"The secret number was: {secret_number}. Better luck next time!")

print("Thanks for playing!")