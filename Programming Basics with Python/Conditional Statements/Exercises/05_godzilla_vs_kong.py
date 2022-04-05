film_budget = float(input())
extras = int(input())
clothing_price_one_extra = float(input())

decor = film_budget * 0.1
price_clothing_total = extras * clothing_price_one_extra


if extras > 150:
    price_clothing_total = price_clothing_total * 0.9

money_left = film_budget - (decor + price_clothing_total)

if decor + price_clothing_total > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(money_left):.2f} leva left.")