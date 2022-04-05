events = input().split("|")

energy = 100
coins = 100
rush_is_over = False

for event in events:
    event_ingredient, number = event.split("-")
    number = int(number)

    if event_ingredient == "rest":
        if energy < 100:
            energy += number
            if energy > 100:
                energy = 100
        else:
            number = 0
            energy = 100
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event_ingredient == "order":
        energy -= 30
        if energy >= 0:
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 80
            print("You had to rest!")
    else:
        if coins > number:
            coins -= number
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            rush_is_over = True
            break

if not rush_is_over:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
