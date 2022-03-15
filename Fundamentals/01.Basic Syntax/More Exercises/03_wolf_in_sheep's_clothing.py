flock_of_sheep = input().split(", ")

wolf = flock_of_sheep.index("wolf")

if wolf == len(flock_of_sheep) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(flock_of_sheep) - (wolf + 1)}! You are about to be eaten by a wolf!")
