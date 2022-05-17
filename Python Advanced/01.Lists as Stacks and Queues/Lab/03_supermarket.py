from collections import deque

queue = deque()

command = input()

while command != "End":
    if command != "Paid":
        queue.append(command)
    if command == "Paid":
        for i in range(len(queue)):
            print(queue.popleft())

    command = input()

print(f"{len(queue)} people remaining.")
