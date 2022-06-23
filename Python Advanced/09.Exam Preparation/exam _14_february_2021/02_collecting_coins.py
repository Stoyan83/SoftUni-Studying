import math


def move_up(row, col, size):
    if row <= 0:
        return size - 1, col
    return row - 1, col


def move_down(row, col, size):
    if row >= size - 1:
        return 0, col
    return row + 1, col


def move_right(row, col, size):
    if col >= size - 1:
        return row, 0
    return row, col + 1


def move_left(row, col, size):
    if col <= 0:
        return row, size - 1
    return row, col - 1


directions = {
    "up": move_up,
    "down": move_down,
    "right": move_right,
    "left": move_left

}

size = int(input())

player_row = 0
player_col = 0

matrix = []

for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col

coins = 0

path = []
over = False

while True:
    command = input()
    current_row, current_col = directions[command](player_row, player_col, size)
    path.append(f"[{player_row}, {player_col}]")
    if matrix[current_row][current_col] == "P":
        matrix[current_row][current_col] = 0
    if matrix[current_row][current_col] == "X":
        coins = math.floor(coins * 0.5)
        over = True
        path.append(f"[{current_row}, {current_col}]")
        break
    else:
        coins += matrix[current_row][current_col]
        matrix[current_row][current_col] = 0
        if coins >= 100:
            path.append(f"[{current_row}, {current_col}]")
            break

    player_row, player_col = current_row, current_col

if not over:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
print(*path, sep="\n")
