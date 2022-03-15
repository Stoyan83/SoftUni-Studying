# Eggs =  1 pack
# Flour = 1 kg
# Milk = 0.250 l

budget = float(input())
price_1kg_floor = float(input())
colored_eggs = 0
breads = 0

price_1pack_eggs = 0.75 * price_1kg_floor
price_1l_milk = price_1kg_floor * 1.25

one_bread_price = price_1kg_floor + price_1pack_eggs + price_1l_milk / 4

while budget >= one_bread_price:
    budget -= one_bread_price
    breads += 1
    colored_eggs += 3
    if breads % 3 == 0:
        colored_eggs -= (breads - 2)

print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")