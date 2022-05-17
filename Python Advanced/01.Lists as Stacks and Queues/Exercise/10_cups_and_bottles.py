from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        cup -= bottle
    wasted_water += abs(cup)

if cups:
    print(f"Cups:", ' '.join([str(x) for x in cups]))
else:
    print(f"Bottles:", ' '.join([str(x) for x in bottles]))

print(f"Wasted litters of water: {wasted_water}")


