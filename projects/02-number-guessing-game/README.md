# Number Guessing Game

A small command-line game built while learning Python fundamentals.

The player has to guess a randomly generated number between 1 and 100 within 10 attempts.

This project started as a simple script and was gradually improved with functions, input validation, a main menu, scoring, and a highscore system.

## What I Built

- Random number generation
- Number guessing loop
- Maximum of 10 attempts
- Input validation
- `q` command to quit
- `menu` command to return to the main menu
- Main menu
- Score system
- Highscore tracking
- Separate functions for different responsibilities

## How It Works

1. The program generates a random number between 1 and 100.
2. The player enters a guess.
3. The program checks whether the input is valid.
4. The player receives a hint:
   - `Too low!`
   - `Too high!`
5. The player has up to 10 attempts.
6. A score is calculated based on how quickly the number is guessed.
7. The highscore is updated when a new highest score is achieved.

## Concepts Practiced

- Variables
- `input()`
- Type conversion with `int()`
- `if / elif / else`
- `while` loops
- `break`
- `continue`
- `return`
- Functions
- Function arguments and return values
- `try / except`
- `ValueError`
- The `random` module
- Global variables
- Basic program structure

## Project Structure

```text
02-number-guessing-game/
└── project1.2.py
└── project1.py