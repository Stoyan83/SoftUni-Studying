def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

size = int(input())

food = 0

matrix = []
snake_row = 0
snake_col = 0
lair = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "S":
            snake_row = row
            snake_col = col
        if matrix[row][col] == "B":
            lair.append((row, col))

matrix[snake_row][snake_col] = "."

while True:
    command = input()
    current_row, current_col = directions[command](snake_row, snake_col)
    if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
        break
    if matrix[current_row][current_col] == "B":
        lair.remove((current_row, current_col))
        matrix[current_row][current_col] = "."
        snake_row, snake_col = lair[0][0], lair[0][1]
        matrix[snake_row][snake_col] = "."
        continue
    if matrix[current_row][current_col] == "*":
        food += 1
        matrix[current_row][current_col] = "."
        if food >= 10:
            matrix[current_row][current_col] = "S"
            break

    snake_row, snake_col = current_row, current_col
    matrix[snake_row][snake_col] = "."

if food < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
for m in matrix:
    print(*m, sep="")
