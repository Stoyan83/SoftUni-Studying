from math import floor, ceil

vineyard = int(input())
grape_per_m2 = float(input())
liters_needed = int(input())
workers = int(input())

area_for_wine = vineyard * 0.4
grape_harvest = area_for_wine * grape_per_m2
total_wine = grape_harvest / 2.5
wine_needed = liters_needed - total_wine
wine_left = total_wine - liters_needed
wine_per_worker = wine_left / workers

if total_wine < liters_needed:
    print(f"It will be a tough winter! More {floor(wine_needed)} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")