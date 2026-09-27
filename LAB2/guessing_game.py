# This program creates a number guessing game.
# The computer selects a number from 1 to 100,
# and the user gets a maximum of 7 attempts to guess it.

import random


def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


def guessing_game():
    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)

    max_attempts = 7

    for attempt in range(1, max_attempts + 1):
        print("\nAttempt", attempt, "of", max_attempts)

        guess = get_guess()

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Correct!")
            print("You guessed the number in", attempt, "attempt(s).")
            return

    print("\nYou have used all 7 attempts.")
    print("The correct number was:", secret_number)
    print("Better luck next time!")


guessing_game()