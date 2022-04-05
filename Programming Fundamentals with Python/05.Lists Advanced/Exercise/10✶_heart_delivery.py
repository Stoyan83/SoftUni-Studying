neighbor = [int(x) for x in input().split("@")]
start_index = 0

command = input()

while not command == "Love!":
    jump, index = command.split()
    index = int(index)
    start_index += index
    if start_index >= len(neighbor):
        start_index = 0
    if neighbor[start_index] > 0:
        neighbor[start_index] -= 2
        if neighbor[start_index] <= 0:
            neighbor[start_index] = 0
            print(f"Place {start_index} has Valentine's day.")

    else:
        print(f"Place {start_index} already had Valentine's day.")

    command = input()
print(f"Cupid's last position was {start_index}.")

neighbor = [x for x in neighbor if x != 0]

if len(neighbor) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbor)} places.")
