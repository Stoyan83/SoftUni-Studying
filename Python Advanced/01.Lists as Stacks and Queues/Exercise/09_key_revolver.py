from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value = int(input())

reload = size_barrel
bullets_shot = 0
success = True

while locks:

    if not bullets or not locks:
        success = False
        break
    else:
        current_bullet = bullets.pop()
        if current_bullet <= locks[0]:
            locks.popleft()
            size_barrel -= 1
            bullets_shot += 1
            print("Bang!")
            if bullets:
                if size_barrel == 0:
                    print("Reloading!")
                    size_barrel = reload

        elif current_bullet > locks[0]:

            print("Ping!")
            size_barrel -= 1
            bullets_shot += 1

            if size_barrel == 0:
                if bullets:
                    print("Reloading!")
                    size_barrel = reload
if success:
    print(f"{len(bullets)} bullets left. Earned ${value - (bullets_shot * bullet_price)}")
else:
    print(F"Couldn't get through. Locks left: {len(locks)}")
