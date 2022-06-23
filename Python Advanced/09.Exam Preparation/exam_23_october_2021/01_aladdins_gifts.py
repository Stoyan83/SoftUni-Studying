from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0
gifts = {"Gemstone" : 0, "Porcelain Sculpture": 0, "Gold" : 0, "Diamond Jewellery": 0}

made = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_material + current_magic
    if result < 100:
        if (current_material + current_magic) % 2 == 0:
            result = current_material * 2 + current_magic * 3
        else:
            result *= 2
    if result > 499:
        result //= 2
    if result < 100 or result > 499:
        continue
    if result in range(100, 200):
        gifts["Gemstone"] += 1
    if result in range(200, 300):
        gifts["Porcelain Sculpture"] += 1
    if result in range(300, 400):
        gifts["Gold"] += 1
    if result in range(400, 500):
        gifts["Diamond Jewellery"] += 1
    if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts['Gold'] > 0 and gifts["Diamond Jewellery"] > 0:
        made = True

if made:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print("Materials left: ", end="")
    print(*materials, sep=", ")
if magic:
    print("Magic left: ", end="")
    print(*magic, sep=", ")

gifts = {x:y for x, y in gifts.items() if y > 0}
sorted_gifts = sorted(gifts.items())
for k, v in sorted_gifts:
    print(f"{k}: {v}")

