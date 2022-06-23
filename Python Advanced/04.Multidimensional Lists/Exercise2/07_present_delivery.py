def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_right(row, col):
    return row, col + 1


def move_left(row, col):
    return row, col - 1


def next_to_cookies(row, col, matrix):
    nice = 0
    bad = 0
    if matrix[row - 1][col] == "V":
        matrix[row - 1][col] = "-"
        nice += 1
    elif matrix[row - 1][col] == "X":
        matrix[row - 1][col] = "-"
        bad += 1
    if matrix[row + 1][col] == "V":
        matrix[row + 1][col] = "-"
        nice += 1
    elif matrix[row + 1][col] == "X":
        matrix[row + 1][col] = "-"
        bad += 1
    if matrix[row][col + 1] == "V":
        matrix[row][col + 1] = "-"
        nice += 1
    elif matrix[row][col + 1] == "C":
        matrix[row][col + 1] = "-"
        bad += 1
    if matrix[row][col - 1] == "V":
        matrix[row][col - 1] = "-"
        nice += 1
    elif matrix[row][col - 1] == "V":
        matrix[row][col - 1] = "-"
        bad += 1
    return matrix, nice, bad


directions = {
    "up": move_up,
    "down": move_down,
    "right": move_right,
    "left": move_left
}

number_of_presents = int(input())
size = int(input())

matrix = []

santa_row = 0
santa_col = 0
total_nice = 0
nice = total_nice

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col
        elif matrix[row][col] == "V":
            total_nice += 1

merry = False

while True:
    command = input()

    if command == "Christmas morning":
        matrix[santa_row][santa_col] = 'S'
        break

    if santa_row >= 0 or santa_col >= 0 or santa_row < size or santa_col < size:
        current_row, current_col = directions[command](santa_row, santa_col)
        if matrix[current_row][current_col] == "V":
            matrix[current_row][current_col] = "-"
            nice += 1
            number_of_presents -= 1
        if matrix[current_row][current_col] == "X":
            matrix[current_row][current_col] = "-"
        if matrix[current_row][current_col] == "C":
            matrix, good, bad = next_to_cookies(current_row, current_col, matrix)
            nice += good
            number_of_presents -= good
            number_of_presents -= bad

        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = current_row, current_col
        if number_of_presents <= 0:
            matrix[santa_row][santa_col] = 'S'
            break

if number_of_presents <= 0 < (total_nice - nice):
    print("Santa ran out of presents!")

for m in matrix:
    print(*m)
if total_nice - nice <= 0:
    print(f"Good job, Santa! {nice} happy nice kid/s.")
else:
    print(f"No presents for {total_nice - nice} nice kid/s.")
