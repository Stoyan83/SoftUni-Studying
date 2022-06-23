def move_up(row, col):
    if row - 1 < 0:
        return 5, col
    return row - 1, col


def move_down(row, col):
    if row + 1 > 5:
        return 0, col
    return row + 1, col


def move_left(row, col):
    if col - 1 < 0:
        return row, 5
    return row, col - 1


def move_right(row, col):
    if col + 1 > 5:
        return row, 0
    return row, col + 1


directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

matrix = []
rover_row = 0
rover_col = 0

for row in range(6):
    current_row = input().split()
    matrix.append(current_row)
    for col in range(6):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

water = 0
concrete = 0
metal = 0

command = input().split(", ")

suitable = False

for i in range(len(command)):

    current_row, current_col = directions[command[i]](rover_row, rover_col)

    if matrix[current_row][current_col] == "R":
        print(f"Rover got broken at ({current_row}, {current_col})")
        break
    elif matrix[current_row][current_col] == "W":
        print(f"Water deposit found at ({current_row}, {current_col})")
        water += 1
        matrix[current_row][current_col] = "-"
    elif matrix[current_row][current_col] == "C":
        print(f"Concrete deposit found at ({current_row}, {current_col})")
        concrete += 1
        matrix[current_row][current_col] = "-"
    elif matrix[current_row][current_col] == "M":
        print(f"Metal deposit found at ({current_row}, {current_col})")
        metal += 1
        matrix[current_row][current_col] = "-"
    if water >= 1 and concrete >= 1 and metal >= 1:
        suitable = True

    rover_row, rover_col = current_row, current_col

if suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")