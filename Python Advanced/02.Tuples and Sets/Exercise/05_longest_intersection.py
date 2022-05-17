import re

n = int(input())
max_length = []
first_set = set()
second_set = set()

for _ in range(n):
    token = re.split(r',|-', input())

    start_first = token[0]
    end_first = token[1]
    start_second = token[2]
    end_second = token[3]

    for i in range(int(start_first), int(end_first) + 1):
        first_set.add(i)

    for j in range(int(start_second), int(end_second) + 1):
        second_set.add(j)

    result = first_set.intersection(second_set)
    if len(result) > len(max_length):
        max_length = list(result)

    first_set = set()
    second_set = set()

print(f"Longest intersection is {max_length} with length {len(max_length)}")
