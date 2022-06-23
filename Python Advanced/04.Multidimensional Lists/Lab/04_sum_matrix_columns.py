# row, column = [int(x) for x in input().split(", ")]
# matrix = []
#
#
# for _ in range(row):
#     matrix.append([int(x) for x in input().split()])
#
# print(*[sum(x) for x in zip(*matrix)], sep="\n")


row, column = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

for c in range(column):
    sum = 0
    for r in range(row):
        sum += matrix[r][c]
    print(sum)
