# This program checks whether a number is an Armstrong number
# and prints all Armstrong numbers within a user-defined range.


def is_armstrong(number):
    if number < 0:
        return False

    digits = len(str(number))
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10

        # Each digit is raised to the power of the number of digits.
        total += digit ** digits
        temp //= 10

    # 0 is also considered an Armstrong number.
    return total == number


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number >= 0:
                return number
            else:
                print("Please enter a non-negative number.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


# Check one number
number = get_positive_integer("Enter a number: ")

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


# Print Armstrong numbers in a range
print("\n--- Armstrong Numbers in a Range ---")

start = get_positive_integer("Enter starting number: ")
end = get_positive_integer("Enter ending number: ")

if start > end:
    print("Starting number must be less than or equal to ending number.")
else:
    armstrong_numbers = []

    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)

    print("Armstrong numbers:", armstrong_numbers)