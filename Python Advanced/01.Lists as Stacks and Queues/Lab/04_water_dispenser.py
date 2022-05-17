from collections import deque

queue = deque()

litters = int(input())

command = input()

while command != 'Start':
    queue.append(command)
    command = input()

command = input()

while command != "End":
    if command.isnumeric():
        current_litters = int(command)
        if litters >= current_litters:
            print(f"{queue.popleft()} got water")
            litters -= current_litters
        else:
            print(f"{queue.popleft()} must wait")

    else:
        _, refill = command.split()
        litters += int(refill)

    command = input()

print(f"{litters} liters left")
