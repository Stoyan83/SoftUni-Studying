def move_up(row, col, size):
    return row - 1, col


def move_down(row, col, size):
    return row + 1, col


def move_right(row, col, size):
    return row, col + 1


def move_left(row, col, size):
    return row, col - 1


directions = {
    "up": move_up,
    "down": move_down,
    "right": move_right,
    "left": move_left
}

name_string = input()

size = int(input())

matrix = []

player_row = 0
player_col = 0

for row in range(size):
    matrix.append([x for x in list(input())])
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col

m = int(input())

for i in range(m):
    command = input()
    current_row, current_col = directions[command](player_row, player_col, size)
    matrix[player_row][player_col] = "-"
    if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
        if name_string:
            name_string = name_string[:len(name_string) - 1]
        current_row, current_col = player_row, player_col
    if matrix[current_row][current_col] != "-":
        name_string += matrix[current_row][current_col]
    matrix[current_row][current_col] = "-"

    player_row, player_col = current_row, current_col

matrix[player_row][player_col] = "P"

print(name_string)
for m in matrix:
    print(*m, sep="")
