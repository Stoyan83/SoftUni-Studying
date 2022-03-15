electrons = int(input())
index = 0
shell = []

while electrons > 0:
    index += 1
    if electrons < 2 * index ** 2:
        shell.append(electrons)
    else:
        shell.append(2 * index ** 2)

    electrons -= (2 * index ** 2)

print(shell)

