trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

price = (puzzles * 2.6) + (talking_dolls * 3) + (teddy_bears * 4.1) + (minions * 8.2) + (trucks * 2)

number_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks

if number_of_toys >= 50:
    total_price = price * 0.75

else:
    total_price = price

total_price_after_rent = total_price * 0.9

money_left = total_price_after_rent - trip_price

if total_price_after_rent >= trip_price:
    print(f"Yes! {abs(money_left):.2f} lv left.")

else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")