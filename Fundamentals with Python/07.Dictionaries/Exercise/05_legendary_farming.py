data = input()

key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

is_farmed = False

while True:
    split_data = data.split()

    for index in range(0, len(split_data), 2):
        quantity = int(split_data[index])
        material = split_data[index + 1].lower()

        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity

        for material, quantity in items.items():
            if quantity >= 250:
                is_farmed = True
                print(f"{key_materials[material]} obtained!")
                items[material] -= 250
                break

        if is_farmed:
            break

    if is_farmed:
        break

    data = input()

for key, value in items.items():
    print(f"{key}: {value}")

for key, value in junk_items.items():
    print(f"{key}: {value}")
