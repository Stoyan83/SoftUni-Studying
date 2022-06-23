row, column = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = -99999999999999999999
square = None

for c in range(column - 1):
    for r in range(row - 1):
        square_sum = [matrix[r][c], matrix[r][c +1],matrix[r + 1][c],matrix[r + 1][c + 1]]
        if sum(square_sum) > max_sum:
            max_sum = sum(square_sum)
            square = square_sum


print(f"{square[0]} {square[1]}")
print(f"{square[2]} {square[3]}")
print(max_sum)
