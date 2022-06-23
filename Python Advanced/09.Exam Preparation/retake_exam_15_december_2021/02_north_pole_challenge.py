def move_up(row, col, matrix_rows, matrix_col):
    if row == 0:
        return  matrix_rows - 1, col
    return row - 1, col

def move_down(row, col, matrix_rows, matrix_col):
    if row == matrix_rows - 1:
        return 0, col
    return row + 1, col


def move_right(row, col, matrix_rows, matrix_cols):
    if col == matrix_cols - 1:
        return row, 0
    return row, col + 1

def move_left(row, col,matrix_rows, matrix_col):
    if col == 0:
        return  row, matrix_col - 1
    return row, col - 1

directions = {
    "up": move_up,
    "down" : move_down,
    "right" : move_right,
    "left" : move_left
}

matrix_rows, matrix_cols = [int(x) for x in input().split(", ")]


matrix = []
decorations = set()
gifts = set()
cookies = set()

decorations_cnt = 0
gifts_cnt = 0
cookies_cnt = 0


player_row = 0
player_col = 0

for row in range(matrix_rows):
    matrix.append([x for x in input().split()])
    for col in range(matrix_cols):
        if matrix[row][col] == "G":
            gifts.add(f"{row} {col}")
            gifts_cnt += 1
        elif matrix[row][col] == "D":
            decorations.add(f"{row} {col}")
            decorations_cnt += 1
        elif matrix[row][col] == "C":
            cookies.add(f"{row} {col}")
            cookies_cnt += 1
        elif matrix[row][col] == "Y":
            player_row = row
            player_col = col

done = False

command = input()

while command != "End":


    direction, steps = command.split("-")


    for _ in range(int(steps)):


        current_row, current_col = directions[direction](player_row, player_col, matrix_rows, matrix_cols)
        if matrix[current_row][current_col] == "G":
            gifts_cnt -= 1

        elif matrix[current_row][current_col] == "D":
            decorations_cnt -= 1

        elif matrix[current_row][current_col] == "C":
            cookies_cnt -= 1



        matrix[player_row][player_col] = "x"
        if decorations_cnt == 0 and gifts_cnt == 0 and cookies_cnt == 0:
            matrix[current_row][current_col] = "Y"
            done = True
            break
        player_row, player_col = current_row, current_col

    if done:
        break
    command = input()



if not done:

    matrix[current_row][current_col] = "Y"
else:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {len(decorations) - decorations_cnt} Christmas decorations")
print(f"- {len(gifts) - gifts_cnt} Gifts")
print(f"- {len(cookies) - cookies_cnt} Cookies")
for r in matrix:
    print(*r, sep = " ")