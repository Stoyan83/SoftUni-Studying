from collections import  deque

line = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": ['red', 'yellow'],
    "purple": ['blue', 'red'],
    "green": ['yellow', 'blue'],
}

formed_colors = []

while line:
    first = line.popleft()
    second = line.pop() if line else ''
    string_result = first + second
    if string_result in all_colors:
        formed_colors.append(string_result)
        continue

    string_result = second + first
    if string_result in all_colors:
        formed_colors.append(string_result)
        continue

    first = first[:-1]
    second = second[:-1]

    if first:
        line.insert(len(line) // 2, first)
    if second:
        line.insert(len(line) // 2, second)

final_colors = []

for color in formed_colors:
    if color in main_colors:
        final_colors.append(color)
        continue

    if color in secondary_colors.keys():
        is_valid = True
        for required_color in secondary_colors[color]:
            if required_color not in formed_colors:
                is_valid = False
                break
        if is_valid:
            final_colors.append(color)

print(final_colors)