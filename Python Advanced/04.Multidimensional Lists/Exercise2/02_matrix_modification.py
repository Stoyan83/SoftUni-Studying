n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != "END":
    action, row, column, value = command.split()
    row = int(row)
    column = int(column)
    value = int(value)

    if 0 > row or row >= len(matrix) - 1 or column >= len(matrix) - 1 or 0 > column:
        print("Invalid coordinates")
        command = input()
        continue

    if action == "Subtract":
        matrix[row][column] -= value
    elif action == "Add":
        matrix[row][column] += value
    command = input()

for i in matrix:
    print(*i)
