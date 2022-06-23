from collections import deque

toys = 0
energy = 0
count = 0

elves = deque([int(x) for x in input().split()])

materials = [int(x) for x in input().split()]

while elves and materials:

    current_energy = elves.popleft()
    current_material = materials.pop()

    if current_energy < 5:
        materials.append(current_material)
        continue

    needed_energy = current_material
    count += 1

    if count % 3 == 0:
        needed_energy = current_material * 2

    if current_energy < needed_energy:
        elves.append(current_energy * 2)
        materials.append(current_material)
        continue

    energy += needed_energy
    current_energy -= needed_energy

    if count % 3 == 0:
        if count % 5 == 0:
            elves.append(current_energy)
        else:
            elves.append(current_energy + 1)
            toys += 2

    elif count % 5 == 0:
        elves.append(current_energy)

    else:
        elves.append(current_energy + 1)
        toys += 1

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elves:
    print("Elves left: ", end="")
    print(*elves, sep=", ")
if materials:
    print("Boxes left: ", end="")
    print(*materials, sep=', ')
