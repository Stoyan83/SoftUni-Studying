number_of_lines = int(input())

tank_capacity = 255

for liter in range(1, number_of_lines + 1):
    liters = int(input())
    if liters < tank_capacity:
        tank_capacity -= liters
    else:
        print("Insufficient capacity!")
print(255 - tank_capacity)