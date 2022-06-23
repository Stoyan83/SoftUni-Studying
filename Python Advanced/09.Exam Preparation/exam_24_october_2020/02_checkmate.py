def is_valid_cell(spot):
    if min(spot) >= 0 and max(spot) < 8:
        return True
    else:
        return False


def capture(row, col, board):
    captured = []

    for i in range(col, len(board) - 1):  # Check right
        if board[row][i + 1] == "Q":
            captured.append(f"[{row}, {i + 1}]")
            break

    for j in range(col, 0, -1):  # Check left

        if board[row][j - 1] == "Q":
            captured.append(f"[{row}, {j - 1}]")
            break

    for k in range(row, len(board) - 1): # Check down
        if board[k + 1][col] == "Q":
            captured.append(f"[{k + 1}, {col}]")
            break

    for l in range(row, 0, -1):  # Check Up
        if board[l - 1][col] == "Q":
            captured.append(f"[{l - 1}, {col}]")
            break

    while row > -1:  # Right up diagonal
        if is_valid_cell([row - 1, col + 1]):
            if board[row - 1][col + 1] == "Q":
                captured.append(f"[{row - 1}, {col + 1}]")
                break
        row -= 1
        col += 1
    row, col = kings_row, kings_col

    while row < len(board) - 1:  # Right down diagonal
        if is_valid_cell([row + 1, col + 1]):
            if board[row + 1][col + 1] == "Q":
                captured.append(f"[{row + 1}, {col + 1}]")
                break
        row += 1
        col += 1
    row, col = kings_row, kings_col

    while row < len(board) - 1:  # Left down diagonal
        if is_valid_cell([row + 1, col - 1]):
            if board[row + 1][col - 1] == "Q":
                captured.append(f"[{row + 1}, {col - 1}]")
                break
        row += 1
        col -= 1
    row, col = kings_row, kings_col

    while row > -1:  # Left up diagonal
        if is_valid_cell([row - 1, col - 1]):
            if board[row - 1][col - 1] == "Q":
                captured.append(f"[{row - 1}, {col - 1}]")
                break
        row -= 1
        col -= 1
    row, col = kings_row, kings_col

    return captured


size = 8

board = []
kings_row = 0
kings_col = 0

for row in range(size):
    board.append([x for x in input().split()])
    for col in range(size):
        if board[row][col] == "K":
            kings_row = row
            kings_col = col

result = capture(kings_row, kings_col, board)

if result:
    for r in result:
        print(r)
else:
    print("The king is safe!")
