import numpy as np

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter elements for Matrix 1:")
A = []
for i in range(m):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != n:
        print(f"Row must have exactly {n} elements.")
        exit()
    A.append(row)

print("Enter elements for Matrix 2:")
B = []
for i in range(m):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != n:
        print(f"Row must have exactly {n} elements.")
        exit()
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\nMatrix 1:")
print(A)

print("\nMatrix 2:")
print(B)

result = A + B

print("\nSum of the matrices:")
print(result)
