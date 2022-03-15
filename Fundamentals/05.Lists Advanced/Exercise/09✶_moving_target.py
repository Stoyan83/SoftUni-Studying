targets = [int(x) for x in input().split()]

command = input()

while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    if action == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    if action == "Strike":
        if index in range(len(targets)):
            if index - value in range(len(targets)) and index + value in range(len(targets)):
                del targets[index - value:index + value + 1]
            else:
                print("Strike missed!")

        # else:
        #     print("Strike missed!")

    command = input()

print(*targets, sep="|")
