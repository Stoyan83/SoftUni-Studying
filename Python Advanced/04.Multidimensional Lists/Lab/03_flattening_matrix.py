n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

print(sum(matrix, []))