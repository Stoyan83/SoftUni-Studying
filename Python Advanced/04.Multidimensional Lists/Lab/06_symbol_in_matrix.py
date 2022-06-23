n = int(input())
matrix = []
found = ()

for _ in range(n):
    matrix.append(list(input()))

symbol = input()

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == symbol:
            found = (r, c)

            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
else:
    print(found)