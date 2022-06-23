row, column = [int(x) for x in input().split()]
matrix = []

for _ in range(row):
    matrix.append([x for x in input().split()])

command = input()
while command != "END":
    try:
        action, first_r, first_c, second_r, second_c = command.split()
        if action == "swap":
            matrix[int(first_r)][int(first_c)], matrix[int(second_r)][int(second_c)] = \
                matrix[int(second_r)][int(second_c)], matrix[int(first_r)][int(first_c)]
            for rows in matrix:
                print(*rows)
    except Exception:
        print("Invalid input!")
    command = input()
