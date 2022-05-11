friends = input().split(", ")
black = []
lost = []

command = input()

while not command == "Report":
    current_command = command.split()
    if current_command[0] == "Blacklist":
        name = current_command[1]
        if name in friends:
            index = friends.index(name)
            friends[index] = "Blacklisted"
            black.append(name)
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif current_command[0] == "Error":
        index = int(current_command[1])
        if index in range(len(friends)):
            if friends[index] != "Blacklisted" and friends[index] != "Lost":
                print(f"{friends[index]} was lost due to an error.")
                lost.append(friends[index])
                friends[index] = "Lost"
    elif current_command[0] == "Change":
        index = int(current_command[1])
        new_name = current_command[2]
        if index in range(len(friends)):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

    command = input()

print(f"Blacklisted names: {len(black)}")
print(f"Lost names: {len(lost)}")
print(*friends)






