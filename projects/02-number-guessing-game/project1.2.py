# Upgraded version of project1.py the number guessing game, with functions and improved structure
# It's still a work in progress, but it has a main menu.
# It have so many bugs and loop holes, but I will fix them in the future.
# I'm planning to add some more features to it. Stay tuned...
import random


current_highscore = 0

def get_guess():
    while True:
        user_input = input("Enter your guess (or 'q' to quit, 'menu' for main menu): ")
        if user_input == "q":
            print("Quitting the game...")
            return "quit"
        elif user_input == "menu":
            print("Returning to the main menu...")
            return "menu"
        
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    global current_highscore
    while True:
        print("Welcome to the Number Guessing Game!")
        print("1. Play the game")
        print("2. View Highscore")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            final_score = play_game()
            
            if final_score > current_highscore:
                current_highscore = final_score
                print(f"New Highscore! Your score is: {current_highscore}")
        elif choice == "2":
            view_highscore()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def play_game():
    secret_number = random.randint(1, 100)
    tries = 0
    print(f"\n[DEBUG] The secret number is {secret_number}") # For debugging purposes
    print("I'm thinking of a number between 1 and 100. You have 10 tries!")
    
    while True:
        guess = get_guess()
        
        if guess == "quit":
            return 0
        elif guess == "menu":
            return 0
        
        tries += 1
        
        if guess == secret_number:
            print(f"Correct! You found it in {tries} tries.")
            
            # Score logic
            if tries == 1:
                return 100
            elif tries < 5:
                return 90
            elif tries < 8:
                return 50
            elif tries < 10:
                return 20
            else:
                return 10
        
        if tries >= 10:
            print(f"You've used all your tries! The correct number was {secret_number}.")
            print("Better luck next time!")
            return 0
            
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

def view_highscore():
    print(f"\nThe current highscore is: {current_highscore} points")


main_menu()
