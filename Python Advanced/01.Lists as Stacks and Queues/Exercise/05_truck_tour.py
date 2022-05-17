from collections import deque

number_of_pumps = int(input())
circle = deque()

for _ in range(number_of_pumps):
    pumps = [int(x) for x in input().split()]
    circle.append(pumps)

for i in range(len(circle)):
    failed = False
    tank = 0
    for fuel, distance in circle:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        circle.append(circle.popleft())
    else:
        print(i)
        break


