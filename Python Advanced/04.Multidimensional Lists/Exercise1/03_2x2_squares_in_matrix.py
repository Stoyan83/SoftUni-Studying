row, column = [int(x) for x in input().split()]
matrix = []

for _ in range(row):
    matrix.append([x for x in input().split()])

count = 0

for c in range(column - 1):
    for r in range(row - 1):
        if matrix[r][c] == matrix[r][c +1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            count += 1

print(count)