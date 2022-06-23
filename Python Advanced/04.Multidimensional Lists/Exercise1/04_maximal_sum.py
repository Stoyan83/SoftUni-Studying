row, column = [int(x) for x in input().split()]
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

max_sum = -99999999999999999999
square = None

for c in range(column - 2):
    for r in range(row - 2):
        square_sum = [matrix[r][c], matrix[r][c + 1],matrix[r][c + 2],
                      matrix[r + 1][c],matrix[r + 1][c + 1], matrix[r + 1][c + 2],
                      matrix[r + 2][c],matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        if sum(square_sum) > max_sum:
            max_sum = sum(square_sum)
            square = square_sum

print(f"Sum = {max_sum}")
print(f"{square[0]} {square[1]} {square[2]}")
print(f"{square[3]} {square[4]} {square[5]}")
print(f"{square[6]} {square[7]} {square[8]}")