rows = int(input())

ships = []
destroyed = 0

for r in range(rows):
    ships.append([int(x) for x in input().split(" ")])

attack = input().split(" ")

for el in attack:
    row = int(el[0])
    column = int(el[2])
    if row in range(0, len(ships)) and column in range(0, len(ships)):
        ships[row][column] -= 1

        if ships[row][column] == 0:
            destroyed += 1

print(destroyed)
