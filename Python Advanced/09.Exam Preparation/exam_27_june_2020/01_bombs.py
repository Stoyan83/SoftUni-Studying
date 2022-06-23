from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]

types = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

produced = {"Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0}

while effects and casings:

    current_production = {x:y for x,y in produced.items() if y >= 3}
    if len(current_production) >= 3:
        break
    result = effects[0] + casings[-1]
    if result not in types.values():
        casings[-1] -= 5
        continue
    else:
        effects.popleft()
        casings.pop()
        for k, v in types.items():
            if v == result:
                produced[k] += 1


if len(current_production) >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print("Bomb Effects: ", end="")
    print(*effects, sep = ", ")
else:
    print("Bomb Effects: empty")
if casings:
    print("Bomb Casings: ", end="")
    print(*casings, sep=", ")
else:
    print("Bomb Casings: empty")
for k, v in sorted(produced.items()):
    print(f"{k}: {v}")

