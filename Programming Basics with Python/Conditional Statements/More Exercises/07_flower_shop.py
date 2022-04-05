from math import floor, ceil

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolia_price = magnolia_count * 3.25
hyacinth_price = hyacinth_count * 4
rose_price = rose_count * 3.5
cactus_price = cactus_count * 8
order_price = magnolia_price + hyacinth_price + rose_price + cactus_price
net_income = order_price * 0.95

if net_income >= present_price:
    money_left = net_income - present_price
    print(f"She is left with {floor(money_left)} leva.")

else:
    money_needed = present_price - net_income
    print(f"She will have to borrow {ceil(money_needed)} leva.")