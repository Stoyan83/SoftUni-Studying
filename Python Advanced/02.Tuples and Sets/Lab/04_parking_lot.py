n = int(input())
parking = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        parking.add(number)
    elif direction == "OUT":
        parking.remove(number)
        
if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")
