n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - i - 1])

result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)
