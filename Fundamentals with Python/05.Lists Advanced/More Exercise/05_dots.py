def check_up(board, row, column):
    if row > 0 and board[row - 1][column] == "." and [row - 1, column] not in visited_indexes:
        return True


def check_down(board, row, column):
    if row < rows - 1 and board[row + 1][column] == "." and [row + 1, column] not in visited_indexes:
        return True


def check_left(board, row, column):
    if column > 0 and board[row][column - 1] == "." and [row, column - 1] not in visited_indexes:
        return True


def check_right(board, row, column):
    if column < columns - 1 and board[row][column + 1] == "." and [row, column + 1] not in visited_indexes:
        return True


rows = int(input())
board = [input().split() for x in range(rows)]
columns = len(board[0])
max_dots = 0

for r in range(rows):
    for c in range(columns):
        if board[r][c] == ".":
            visited_indexes = []
            row = r
            column = c
            dots_connected = 0

            while True:
                if board[row][column] == "-":
                    break

                elif check_right(board, row, column):
                    visited_indexes.append([row, column])
                    column += 1

                elif check_left(board, row, column):
                    visited_indexes.append([row, column])
                    column -= 1

                elif check_up(board, row, column):
                    visited_indexes.append([row, column])
                    row -= 1

                elif check_down(board, row, column):
                    visited_indexes.append([row, column])
                    row += 1

                else:
                    board[row][column] = "-"
                    visited_indexes = []
                    dots_connected += 1
                    row = r
                    column = c

                    if dots_connected > max_dots:
                        max_dots = dots_connected

print(max_dots)