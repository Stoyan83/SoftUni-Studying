from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
signs = deque(input().split())

total_honey = 0

while bees and nectar:

    current_bee = bees[0]
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        try:
            result = abs(eval(str(bees.popleft()) + signs.popleft() + str(current_nectar)))
            total_honey += result
        except:
            pass

print(f"Total honey made: {total_honey}")
if bees:
    print("Bees left: ", end="")
    print(*bees, sep=", ")
if nectar:
    print("Nectar left: ", end="")
    print(*nectar, sep=", ")
