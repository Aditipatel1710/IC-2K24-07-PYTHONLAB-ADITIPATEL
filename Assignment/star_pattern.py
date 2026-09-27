n = int(input("Enter n: "))

# outer loop for rows
for i in range(1, n + 1):
    # inner loop for stars
    for j in range(i):
        print("*", end="")
    print()