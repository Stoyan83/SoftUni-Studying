def is_inside(row, col, matrix):
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
        return True
    return False


def moving(row, col, matrix):
    moves = [0, 1, 0, -1, 1, 0, -1, 0]

    for i in range(0, len(moves), 2):
        if is_inside(row + moves[i], col + moves[i + 1], matrix):
            if matrix[row + moves[i]][col + moves[i + 1]] == " ":
                return row + moves[i], col + moves[i + 1]
    for i in range(0, len(moves), 2):
        if not is_inside(row + moves[i], col + moves[i + 1], matrix):
            return -1, - 1

    return -2, -2


size = int(input())

matrix = []
kates_row = 0
kates_col = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(len(matrix[row])):
        if matrix[row][col] == "k":
            kates_row = row
            kates_col = col

moves = 0
out = False

while True:
    current_row, current_col = moving(kates_row, kates_col, matrix)

    matrix[kates_row][kates_col] = "."
    moves += 1

    if current_row == -1:
        out = True
        break
    if current_row == -2:
        break

    kates_row, kates_col = current_row, current_col

if out:
    print(f"Kate got out in {moves} moves")
else:
    print("Kate cannot get out")
