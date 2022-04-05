number_of_wagons = int(input())
train = [int(x) * 0 for x in range(number_of_wagons)]

command = input()

while not command == "End":
    current_command = command.split()
    if current_command[0] == "add":
        train[-1] += int(current_command[1])
    elif current_command[0] == "insert":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] += people
    elif current_command[0] == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] -= people

    command = input()

print(train)
