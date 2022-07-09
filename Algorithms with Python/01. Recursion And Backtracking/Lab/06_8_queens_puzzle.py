def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queens(row, col, rows, cols, left_diagonalss, right_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonalss:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(row, col, board, rows, cols, left_diagonalss, right_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonalss.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diagonalss, right_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonalss.remove(row - col)
    right_diagonals.remove(row + col)


def put_queens(row, board, rows, cols, left_diagonalss, right_diagonals):
    if row == 8:
        print_board(board)
        return
    for col in range(n):
        if can_place_queens(row, col, rows, cols, left_diagonalss, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonalss, right_diagonals)
            put_queens(row + 1, board, rows, cols, left_diagonalss, right_diagonals)
            remove_queen(row, col, board, rows, cols, left_diagonalss, right_diagonals)


n = 8
board = []
[board.append(["-"] * n) for _ in range(n)]

put_queens(0, board, set(), set(), set(), set())
