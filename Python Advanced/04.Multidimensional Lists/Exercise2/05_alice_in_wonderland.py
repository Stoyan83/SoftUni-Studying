def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_right(row, col):
    return row, col + 1


def move_left(row, col):
    return row, col - 1


directions = {
    "up": move_up,
    "down": move_down,
    "right": move_right,
    "left": move_left

}

size = int(input())
matrix = []
alice_row = 0
alice_col = 0
tea_bags = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col

made_it = False

while True:
    command = input()

    matrix[alice_row][alice_col] = "*"
    current_row, current_col = directions[command](alice_row, alice_col)
    if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
        break

    if matrix[current_row][current_col] == "R":
        matrix[current_row][current_col] = "*"
        break

    elif matrix[current_row][current_col].isdigit():
        tea_bags += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = "*"

    matrix[current_row][current_col] = "*"
    alice_row, alice_col = current_row, current_col

    if tea_bags >= 10:
        made_it = True
        break

if made_it:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for i in matrix:
    print(*i)
