N = int(input("Enter N: "))
matrix = []

for i in range(N):
    row = []
    for j in range(N):
        if i % 2 == 0:
            row.append(i + 1)
        else:
            row.append(-j - 1)
    matrix.append(row)

for row in matrix:
    for num in row:
        print(f"{num:4}", end="")
    print()

