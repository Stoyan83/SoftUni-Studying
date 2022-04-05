number_of_rooms = int(input())
room_count = 0
total_chairs = 0
free_chairs = True

for nums in range(number_of_rooms):
    chairs, visitors = input().split()
    room_count += 1
    total_chairs += len(chairs) - int(visitors)
    if len(chairs) < int(visitors):
        print(f"{int(visitors) - len(chairs) } more chairs needed in room {room_count}")
        free_chairs = False

if free_chairs:
    print(f"Game On, {total_chairs} free chairs left")




