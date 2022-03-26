structure = {}

command = input()

while not command == "End":
    current_command = command.split(" -> ")
    if current_command[0] not in structure:
        structure[current_command[0]] = []
    if current_command[1] not in structure[current_command[0]]:
        structure[current_command[0]].append(current_command[1])

    command = input()

for key, value in structure.items():
    print(f"{key}")
    print("-- ", end="")
    print(*value, sep="\n" "-- ")

print(structure)
