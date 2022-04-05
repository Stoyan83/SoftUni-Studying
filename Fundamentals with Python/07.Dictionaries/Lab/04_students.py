command = input().split(":")
students = {}

while len(command) > 1:
    key = command[2]
    if key not in students:
        students[key] = [command[0]]
        students[key].append(command[1])
    else:
        students[key].append(command[0])
        students[key].append(command[1])

    command = input().split(":")

if len(command) == 1:

    current_command = "".join(command)
    new = current_command.replace("_", " ")
    if new in students.keys():
        for i in range(0, len(students[new]), 2):
            print(f"{students[new][i]} - {students[new][i + 1]}")
 