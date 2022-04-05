command = input().split("#")
water = int(input())
effort = 0
fire_counter = 0
cells = []
for fire in command:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if water < value:
        continue

    if fire_type == "High":

        if 81 <= value <= 125:
            cells.append(value)
            effort += int(value) * 0.25
            fire_counter += int(value)
            water -= int(value)

    elif fire_type == "Medium":
        if 51 <= value <= 80:
            cells.append(value)
            effort += value * 0.25
            fire_counter += value
            water -= value
            
    elif fire_type == "Low":
        if 1 <= value <= 50:
            cells.append(value)
            effort += int(value) * 0.25
            fire_counter += value
            water -= value

print("Cells:")
for i in range(len(cells)):
    print(f" - {cells[i]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_counter}")
