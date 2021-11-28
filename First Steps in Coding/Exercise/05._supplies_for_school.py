number_pen_packs = int(input())
number_marker_packs = int(input())
liters_cleaning_product = int(input())
discount = int(input())
price_one_pens_pack = 5.8
markers_pack_price = 7.2
liter_cleaning_product_price = 1.2

price_pen_packs = number_pen_packs * price_one_pens_pack
price_marker_packs = number_marker_packs * markers_pack_price
price_cleaning_product = liters_cleaning_product * liter_cleaning_product_price

sum = price_pen_packs +price_marker_packs + price_cleaning_product

total_sum = sum -(sum * discount/100)

print(f'{total_sum:.2f}')
