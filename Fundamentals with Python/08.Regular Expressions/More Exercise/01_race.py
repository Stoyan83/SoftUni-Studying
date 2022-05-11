import re

participants = {i: 0 for i in input().split(", ")}
filtered_participants = []

pattern = r"[A-Za-z0-9]+"

info = input()

while not info == "end of race":
    match = re.findall(pattern, info)
    filtered_participants.append("".join(match))

    info = input()

for p in filtered_participants:
    name = ""
    distance = 0
    for ch in p:
        if ch.isalpha():
            name += ch
        if ch.isdigit():
            distance += int(ch)
    if name in participants:
        participants[name] += distance

sort_dict = sorted(participants.items(), key=lambda x: x[1], reverse=True)[:3]

print(f'1st place: {sort_dict[0][0]}\n2nd place: {sort_dict[1][0]}\n3rd place: {sort_dict[2][0]}')
print(sort_dict)