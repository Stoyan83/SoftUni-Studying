from collections import deque

milkshakes = 0

chocolate = [int(x) for x in input().split(", ")]
cups = deque(int(x) for x in input().split(", "))

while chocolate and cups:

    choco, cup = chocolate.pop(), cups.popleft()

    if min(choco, cup) <= 0:
        if choco > 0: chocolate.append(choco)
        if cup > 0: cups.appendleft(cup)
        continue

    if choco == cup:
        milkshakes += 1
        if milkshakes == 5: break
    else:
        cups.append(cup)
        chocolate.append(choco - 5)

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print("Chocolate: ", end="")
    print(*chocolate, sep=", ")
else:
    print("Chocolate: empty")

if cups:
    print("Milk: ", end="")
    print(*cups, sep=", ")
else:
    print("Milk: empty")
