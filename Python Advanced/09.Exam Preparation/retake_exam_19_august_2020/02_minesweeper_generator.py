# def is_inside (row, col, matrix):
#     if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix):
#         return True
#     return  False
#
#
# def calculate_number(row, col, matrix):
#     count = 0
#     if is_inside(row -1, col, matrix): # Up
#         if matrix[row - 1][col] == "*":
#             count += 1
#     if is_inside(row + 1 , col, matrix): # Down
#         if matrix[row + 1][col] == "*":
#             count += 1
#     if is_inside(row, col + 1, matrix): # Right
#         if matrix[row][col + 1] == "*":
#             count += 1
#     if is_inside(row, col - 1, matrix): # Left
#         if matrix[row][col - 1] == "*":
#             count += 1
#     if is_inside(row - 1, col - 1, matrix):  # Left up diagonal
#         if matrix[row - 1][col - 1] == "*":
#             count += 1
#     if is_inside(row - 1, col + 1, matrix):  # Right up diagonal
#         if matrix[row - 1][col + 1] == "*":
#             count += 1
#     if is_inside(row + 1, col + 1, matrix):  # Right down diagonal
#         if matrix[row + 1][col + 1] == "*":
#             count += 1
#     if is_inside(row + 1, col - 1, matrix):  # Left down diagonal
#         if matrix[row + 1][col - 1] == "*":
#             count += 1
#
#     return count
#
# size = int(input())
# n_mines = int(input())
#
# matrix =[]
#
# for row in range(size):
#     row = []
#     matrix.append(row)
#     for col in range(size):
#         row.append("-")
#
# for m in range(n_mines):
#     mines = input().replace("(","").replace(")","")
#
#     mine_row, mine_col = [int(x) for x in mines.split(", ")]
#     matrix[mine_row][mine_col] = "*"
#
#
#
# for rows in range(size):
#     for cols in range(size):
#         if matrix[rows][cols] != "*":
#             matrix[rows][cols] = calculate_number(rows, cols, matrix)
#
#
# for m in matrix:
#     print(*m, sep=" ")

def is_inside(row, col, matrix):
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix):
        return True
    return False


def calculate_number(row, col, matrix):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if is_inside(row + r, col + c, matrix):
                if matrix[row + r][col + c] == "*":
                    count += 1

    return count


size = int(input())
n_mines = int(input())

matrix = []

for row in range(size):
    row = []
    matrix.append(row)
    for col in range(size):
        row.append("-")

for m in range(n_mines):
    mines = input().replace("(", "").replace(")", "")

    mine_row, mine_col = [int(x) for x in mines.split(", ")]
    matrix[mine_row][mine_col] = "*"

for rows in range(size):
    for cols in range(size):
        if matrix[rows][cols] != "*":
            matrix[rows][cols] = calculate_number(rows, cols, matrix)

for m in matrix:
    print(*m, sep=" ")
