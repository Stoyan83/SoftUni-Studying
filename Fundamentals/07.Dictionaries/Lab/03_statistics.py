command = input()
stock = {}

while not command == "statistics":
    current_command = command.split(": ")
    key = current_command[0]
    value = int(current_command[1])
    if current_command[0] not in stock:
        stock[key] = value
    else:
        stock[key] += value

    command = input()

print("Products in stock:")
for key, value in stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
