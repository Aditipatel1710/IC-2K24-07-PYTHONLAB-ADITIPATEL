n = int(input("Enter odd n: "))

# validation
if n % 2 == 0:
    print("Please enter an odd number")
else:
    mid = n // 2
    
    # upper part + middle
    for i in range(mid + 1):
        # spaces before first star
        for s in range(mid - i):
            print(" ", end="")
        
        print("*", end="")
        
        # inner spaces - only from 2nd row
        if i > 0:
            for s in range(2 * i - 1):
                print(" ", end="")
            print("*", end="")
        
        print()

    # lower part
    for i in range(mid - 1, -1, -1):
        for s in range(mid - i):
            print(" ", end="")
        
        print("*", end="")
        
        if i > 0:
            for s in range(2 * i - 1):
                print(" ", end="")
            print("*", end="")
        
        print()