n = int(input("Enter n: "))

# Upper part - increasing
for i in range(1, n + 1):
    # left stars
    for j in range(i):
        print("*", end="")
    
    # middle spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    # right stars
    for j in range(i):
        print("*", end="")
    
    print()

# Lower part - decreasing
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    for j in range(i):
        print("*", end="")
    
    print()