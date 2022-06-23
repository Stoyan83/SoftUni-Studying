from collections import deque

effects = deque([int(x) for x in input().split(", ")])
power = [int(x) for x in input().split(", ")]

firework = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
done = False
while effects and power:
    current_effect = effects.popleft()

    if current_effect <= 0:
        continue
    current_power = power.pop()
    if current_power <= 0:
        effects.appendleft(current_effect)
        continue

    total = current_effect + current_power

    if total % 5 != 0 and total % 3 != 0:
        effects.append(current_effect - 1)
        power.append(current_power)

        continue

    if total % 5 != 0 and total % 3 == 0:
        firework["Palm Fireworks"] += 1
    elif total % 5 == 0 and total % 3 != 0:
        firework["Willow Fireworks"] += 1
    elif total % 5 == 0 and total % 3 == 0:
        firework["Crossette Fireworks"] += 1

    final_fireworks = {x: y for x, y in firework.items() if y >= 3}
    if len(final_fireworks) == 3:
        done = True
        break

if done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print("Firework Effects left: ", end="")
    print(*effects, sep=", ")
if power:
    print("Explosive Power left: ", end="")
    print(*power, sep=", ")
for k, v in firework.items():
    print(f"{k}: {v}")
