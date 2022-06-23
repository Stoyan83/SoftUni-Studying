
n = int(input())
matrix = []
sum = 0

for i in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(len(matrix)):
    sum += matrix[i][i]

print(sum)
