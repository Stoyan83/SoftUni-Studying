size = 7

players = {1: 501, 2: 501}
throws = {1: 0, 2: 0}

matrix = []

player1, player2 = [x for x in input().split(", ")]
names = {1: player1, 2: player2}

for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])

player_num = 1

while players[1] > 0 and players[2] > 0:
    player_num = 2 if player_num % 2 == 0 else 1
    throws[player_num] += 1
    current_shot = input().replace('(', "").replace(')', "")
    current_row, current_col = [int(x) for x in current_shot.split(", ")]
    if 0 <= current_row < size and 0 <= current_col < size:
        if matrix[current_row][current_col] == "B":
            print(f"{names[player_num]} won the game with {throws[player_num]} throws!")
            break
        elif matrix[current_row][current_col] == "D":
            players[player_num] -= (matrix[current_row][0] + matrix[current_row][size - 1]
                                    + matrix[0][current_col] + matrix[size - 1][current_col]) * 2

        elif matrix[current_row][current_col] == "T":
            players[player_num] -= (matrix[current_row][0] + matrix[current_row][size - 1]
                                    + matrix[0][current_col] + matrix[size - 1][current_col]) * 3
        else:
            players[player_num] -= matrix[current_row][current_col]

    player_num += 1

players = {x: y for x, y in players.items() if y <= 0}
for k, v in players.items():
    print(f"{names[k]} won the game with {throws[k]} throws!")
