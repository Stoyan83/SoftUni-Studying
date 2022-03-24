fuel = input()
liters = float(input())
club_card = input()

price = 0

if fuel == "Gasoline":

    if club_card == "Yes":
        price = (liters * 2.22) - (liters * 0.18)

    elif club_card == "No":
        price = liters * 2.22

elif fuel == "Diesel":

    if club_card == "Yes":
        price = (liters * 2.33) - (liters * 0.12)

    elif club_card == "No":
        price = liters * 2.33

elif fuel == "Gas":

    if club_card == "Yes":
        price = (liters * 0.93) - (liters * 0.08)

    elif club_card == "No":
        price = liters * 0.93

if 20 <= liters <= 25:
    price *= 0.92

elif liters > 25:
    price *= 0.90

print(f"{price:.2f} lv.")