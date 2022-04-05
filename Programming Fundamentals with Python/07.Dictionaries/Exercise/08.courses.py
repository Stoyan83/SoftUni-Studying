uni = {}

command = input()

while command != "end":
    current_command = command.split(" : ")
    if current_command[0] not in uni:
        uni[current_command[0]] = []
    uni[current_command[0]].append(current_command[1])

    command = input()

for key, value in uni.items():
    print(f"{key}: {len(value)}")
    print("-- ", end="")
    print(*value, sep="\n" "-- ")

