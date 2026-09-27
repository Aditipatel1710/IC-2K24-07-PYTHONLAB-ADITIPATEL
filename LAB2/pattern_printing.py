# This program takes the number of rows from the user
# and prints three different patterns using nested loops.


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


n = get_positive_integer("Enter the number of rows: ")


# Pattern 1: Right-angled triangle
print("\n1. Right-Angled Triangle")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Pattern 2: Number pattern
print("\n2. Number Pattern")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Pattern 3: Centered pyramid
print("\n3. Centered Pyramid")

for i in range(1, n + 1):

    # Print spaces first to move the stars toward the center.
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()