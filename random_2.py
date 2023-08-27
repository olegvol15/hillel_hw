import random

N = int(input("Enter N: "))
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]

for row in matrix:
    for num in row:
        print(f"{num:4}", end="")
    print()

diagonal_sum = sum(matrix[i][i] for i in range(N))
print(f"Diagonal sum: {diagonal_sum}")

last_column_sum = sum(row[-1] for row in matrix)
print(f"Last column sum: {last_column_sum}")
