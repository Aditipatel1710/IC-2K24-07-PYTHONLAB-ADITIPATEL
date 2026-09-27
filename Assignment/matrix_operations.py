print("Enter 3x3 Matrix (3 numbers per row):")
matrix = []

# Input using loops
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    if len(row)!= 3:
        print("Please enter exactly 3 numbers!")
        exit()
    matrix.append(row)

# 1. Display matrix in proper form
print("\n1. Matrix in row-column form:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# 2. Sum of all elements
total_sum = 0
for i in range(3):
    for j in range(3):
        total_sum += matrix[i][j]
print(f"\n2. Sum of all elements: {total_sum}")

# 3. Sum of main diagonal
diag_sum = 0
for i in range(3):
    diag_sum += matrix[i][i]
print(f"\n3. Sum of main diagonal: {diag_sum}")

# 4. Largest and smallest
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print(f"\n4. Largest element: {largest}")
print(f" Smallest element: {smallest}")

# 5. Transpose
print("\n5. Transpose of matrix:")
transpose = []
for i in range(3):
    trans_row = []
    for j in range(3):
        trans_row.append(matrix[j][i])
    transpose.append(trans_row)

for i in range(3):
    for j in range(3):
        print(transpose[i][j], end=" ")
    print()