chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price_chicken = chicken_menus * 10.35
price_fish = fish_menus * 12.4
price_vegetarian = vegetarian_menus * 8.15

sum_menus = price_chicken + price_fish + price_vegetarian

desert_price = sum_menus * 0.20
delivery = 2.5

sum_order = sum_menus + desert_price + delivery

print(f"{sum_order:.2f}")
