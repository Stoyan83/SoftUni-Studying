row, column = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split(", ")])

print(sum(sum(matrix, [])))
print(matrix)