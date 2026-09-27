# Reverse Guessing Game
# The computer guesses the number thought of by the user.

print("===== REVERSE GUESSING GAME =====")

low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

if low >= high:
    print("Invalid range!")
else:
    print(f"\nThink of a number between {low} and {high}.")
    print("Do not tell the computer your number.")
    print("Respond with: h = too high, l = too low, c = correct")

    guesses = 0

    while low <= high:
        guess = (low + high) // 2
        guesses += 1

        print(f"\nComputer's guess: {guess}")
        response = input("Your response (h/l/c): ").lower()

        if response == "c":
            print(f"\nComputer guessed your number in {guesses} guesses!")
            break

        elif response == "h":
            # Computer's guess is too high
            high = guess - 1

        elif response == "l":
            # Computer's guess is too low
            low = guess + 1

        else:
            print("Invalid response! Enter h, l, or c.")

    else:
        print("\nYour responses were inconsistent.")