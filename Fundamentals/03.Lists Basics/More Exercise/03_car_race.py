car_times = [int(el) for el in input().split()]
first_car = 0
second_car = 0

half_list = len(car_times) // 2

for first_time in range(half_list):
    if car_times[first_time] == 0:
        first_car *= 0.8
    first_car += car_times[first_time]
for second_time in range(len(car_times) - 1, half_list, -1):
    if car_times[second_time] == 0:
        second_car *= 0.8
    second_car += car_times[second_time]

if first_car < second_car:
    print(f"The winner is left with total time: {first_car:.1f}")
elif first_car > second_car:
    print(f"The winner is right with total time: {second_car:.1f}")




