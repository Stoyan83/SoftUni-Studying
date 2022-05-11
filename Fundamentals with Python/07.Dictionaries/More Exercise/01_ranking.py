line = input()
contest = {}
students = {}

while not line == "end of contests":
    current_line = line.split(":")
    contest[current_line[0]] = current_line[1]

    line = input()

command = input()

while not command == "end of submissions":
    current_command = command.split("=>")

    if current_command[0] in contest and current_command[1] in contest.values():
        if current_command[2] not in students:
            students[current_command[2]] = {current_command[0]: int(current_command[3])}
        else:
            if current_command[0] in students[current_command[2]]:
                if students[current_command[2]][current_command[0]] < int(current_command[3]):
                    students[current_command[2]][current_command[0]] = int(current_command[3])
            else:
                students[current_command[2]][current_command[0]] = int(current_command[3])

    command = input()

ordered_ratings = {n: v for n, v in (sorted(students.items()))}
for key, value in ordered_ratings.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    ordered_ratings[key] = v

max_points = 0
best_candidate = ''

for key, value in ordered_ratings.items():
    current_points = 0
    for sk, sv in value.items():
        current_points += sv
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in ordered_ratings.items():
    print(key)
    for c, p in value.items():
        print(f"#  {c} -> {p}")
