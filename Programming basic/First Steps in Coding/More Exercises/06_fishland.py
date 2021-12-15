mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
bluefin_tuna_kg = float(input())
mussels_kg = float(input())
bonito_price = mackerel_price * 1.6
bluefin_tuna_price = sprat_price * 1.8
mussels_price = 7.5

total_cost = bonito_kg * bonito_price + bluefin_tuna_kg * bluefin_tuna_price + mussels_kg * mussels_price
print(f'{total_cost:.2f}')
