# rows, columns = [int(x) for x in input().split()]
# snake = input()
# index = 0
#
# for row in range(rows):
#     elements = []
#     for col in range(columns):
#         elements.append(snake[index % len(snake)])
#         index += 1
#     if row % 2 == 0:
#         print(*elements, sep="")
#     else:
#         print(*reversed(elements), sep="")

rows, columns = [int(x) for x in input().split()]
snake = input()

index = 0
elements = []

for row in range(rows):
    elements = [None] * columns
    if row % 2 == 0:
        for col in range(columns):
            elements[col] = snake[index % len(snake)]
            index += 1
    else:
        for col in range(columns - 1, - 1, -1):
            elements[col] = snake[index % len(snake)]
            index += 1

    print(*elements, sep="")

print(index)