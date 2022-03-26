mine = {}

command = input()

while not command == "stop":
    if command not in mine:
        mine[command] = int(input())
    else:
        mine[command] += int(input())

    command = input()

for key, value in mine.items():
    print(f"{key} -> {value}")
