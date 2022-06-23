def is_knight(row, col, matrix):
    return matrix[row][col] == "K"


def inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def knight_atack_counter(row, col, matrix):
    result = 0
    # -2, -1
    if inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    # -2, 1
    if inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    # -1, -2
    if inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    # -1, 2
    if inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    # 1, -2
    if inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    # 1, 2
    if inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    # 2, -1
    if inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    # 2, 1
    if inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1

    return result


n = int(input())
board_matrix = []


removed_knights = 0

for _ in range(n):
    board_matrix.append(list(input()))

while True:
    table = {}
    for r in range(len(board_matrix)):
        for c in range(len(board_matrix[r])):
            if board_matrix[r][c] == "0":
                continue
            counter = knight_atack_counter(r, c, board_matrix)
            if counter:
                table[(r, c)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coord, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coord[0]
            knight_col = coord[1]
    board_matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)
