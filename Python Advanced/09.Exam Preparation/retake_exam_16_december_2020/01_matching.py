from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while females and males:
    current_male = males.pop()
    if current_male <= 0:
        continue
    if current_male % 25 == 0:
        current_male = males.pop()
        continue
    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_female % 25 == 0:
        males.append(current_male)
        current_female = females.popleft()
        continue
    if current_male == current_female:
        matches += 1
        continue
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")
if males:
    print("Males left: ", end="")
    print(*males[::-1], sep=", ")
else:
    print("Males left: ", end="")
    print("none")
if females:
    print("Females left: ", end="")
    print(*females, sep=", ")
else:
    print("Females left: ", end="")
    print("none")
