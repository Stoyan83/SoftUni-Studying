first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    location = command[1]
    if action == "Add":
        command = [int(x) for x in command[2:]]
        if location == "First":
            first_sequence.update(command)
        elif location == "Second":
            second_sequence.update(command)
    elif action == "Remove":
        command = [int(x) for x in command[2:]]
        if location == "First":
            first_sequence = set(int(x) for x in first_sequence if x not in command)
        elif location == "Second":
            second_sequence = set(int(x) for x in second_sequence if x not in command)
    elif action == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

first_sequence = sorted(list(first_sequence))
second_sequence = sorted(list(second_sequence))

print(*first_sequence, sep = ", ")
print(*second_sequence, sep = ", ")