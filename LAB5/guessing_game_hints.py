# Guessing Game with Hints and Scoring

import random

secret_number = random.randint(1, 100)

score = 100
max_attempts = 7

print("===== GUESSING GAME =====")
print("Guess a number between 1 and 100.")
print("You have 7 attempts.")
print("You start with 100 points.")
print("Each wrong guess deducts 10 points.\n")

for attempt in range(1, max_attempts + 1):

    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("\nCongratulations! You guessed the correct number!")
        print("Final Score:", score)
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    # Hints after wrong guess
    if secret_number % 2 == 0:
        print("Hint: The secret number is even.")
    else:
        print("Hint: The secret number is odd.")

    if secret_number % 5 == 0:
        print("Hint: The secret number is a multiple of 5.")
    else:
        print("Hint: The secret number is not a multiple of 5.")

    score -= 10
    print("Current Score:", score)

else:
    score = 0
    print("\nYou lost!")
    print("The secret number was:", secret_number)
    print("Final Score:", score)