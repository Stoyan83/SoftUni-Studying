nylon_square_meters = int(input())
paint_liters = int(input())
thinner_liters = int(input())
hours_painters_work = int(input())

price_nylon = (nylon_square_meters + 2) * 1.5
price_paint = (paint_liters + paint_liters * 0.1) * 14.5
price_thinner = thinner_liters * 5
prce_for_bags = 0.4

sum_materials = price_nylon + price_paint + price_thinner + prce_for_bags
price_painters = (sum_materials * 0.3) * hours_painters_work
total_sum = sum_materials + price_painters

print(total_sum)
