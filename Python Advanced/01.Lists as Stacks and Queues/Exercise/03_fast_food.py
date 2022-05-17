from collections import deque

food_quantity = int(input())

nums = [int(x) for x in input().split()]
queue = deque(nums)
biggest_food = max(queue)
complete = True

for _ in range(len(queue)):
    if queue[0] <= food_quantity:
        food_quantity -= queue.popleft()
    else:
        queue = list(str(x) for x in queue)
        print(biggest_food)
        print(f'Orders left: ' + " ".join(queue))
        complete = False
        break

if complete:
    print(biggest_food)
    print("Orders complete")
