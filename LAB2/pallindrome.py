# This program checks whether a number and a string are palindromes.
# The number palindrome is checked using arithmetic operations only.


def is_number_palindrome(number):
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10

        # Build the reversed number digit by digit.
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


def is_string_palindrome(text):
    # Convert to lowercase so that uppercase and lowercase
    # letters are treated as the same.
    text = text.lower()

    return text == text[::-1]


def get_integer(message):
    while True:
        try:
            number = int(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter a non-negative number.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


# Number palindrome
number = get_integer("Enter a number: ")

if is_number_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")


# String palindrome
text = input("\nEnter a string: ")

if is_string_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")