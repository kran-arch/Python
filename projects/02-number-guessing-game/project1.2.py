# upgraded version of project1.py the number guessing game, with functions and improved structure
# its still a work in progress, but it has a main menu and a high score system. 
# The high score system is not fully implemented yet, but it will be in the future.
# IT have so many bugs and loop holes, but I will fix them in the future.
import random

def get_guess():
    while True:
        user_input = input("Enter your guess: ")
        if user_input == "q":
            print("Quitting the game...")
            return None
        elif user_input == "menu":
           print("Returning to the main menu...")
           return None
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("1. Play the game")
        print("2. High scores")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            high_scores()
            # Placeholder for high scores functionality
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def play_game():
    secret_number = random.randint(1, 100)
    tries = 0
    print(f"The secret number is {secret_number}") # for debugging.
    while True:

        guess = get_guess()
        
        if guess is None:
            print("The player quit.")
            break
        
        tries += 1

        if guess == secret_number:
            print("Correct!")
            user_preference()


        if tries >= 10:
            print(f"You've used all your tries! The correct number was {secret_number}.")
            print("Better luck next time!")
            user_preference()
        
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

def user_preference():
    while True:
        preference = input("Do you want to play again? (y/n): ")
        if preference == "y":
            play_game()
            break
        elif preference == "n":
            print("Returning to the main menu...")
            main_menu()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def high_scores():
    
    tries = play_game()
    if tries == 1:
        score = 100
    elif tries <= 5:
        score = 50
    else:
        score = 10

    print(f"Score: {score}")
    ...
    print(f"Your score is: {score}")
    pass

main_menu()