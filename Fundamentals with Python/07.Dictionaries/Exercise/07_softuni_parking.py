number_of_commands = int(input())
parking = {}

for i in range(number_of_commands):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate = command[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")