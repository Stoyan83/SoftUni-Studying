number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    name = input()
    earned_money = float(input())
    owner_expenses = float(input())
    if city % 3 == 0 and city % 5 != 0:
        owner_expenses *= 1.5
    if city % 5 == 0:
        earned_money *= 0.9
    total_profit += earned_money
    total_profit -= owner_expenses


    print(f"In {name} Burger Bus earned {earned_money - owner_expenses:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")

