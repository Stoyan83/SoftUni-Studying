gifts = input().split()

command = input()

while not command == "No Money":
    action = command.split()
    if action[0] == "OutOfStock":
        if action[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == action[1]:
                    gifts[i] = "None"
    elif action[0] == "Required":
        if int(action[2]) in range(len(gifts)):
            gifts[int(action[2])] = action[1]
    elif action[0] == "JustInCase":
        gifts[-1] = action[1]

    command = input()

for j in range(len(gifts)):
    if "None" in gifts:
        gifts.remove("None")

print(*gifts)
