items_collection = input().split("|")
budget = int(input())
profit = 0
sold_items = []
ticket = False


for item in items_collection:
    item_type, price = item.split("->")
    price = float(price)
    sold = [float(el) for el in sold_items]


    if budget + sum(sold) >= 150:
        ticket = True

    if item_type == "Clothes":
        if price <= 50 and price <= budget:
            profit += price * 0.4
            budget -= price
            sold_items.append(f"{price * 1.4:.2f}")
    elif item_type == "Shoes":
        if price <= 35 and price <= budget:
            profit += price * 0.4
            budget -= price
            sold_items.append(f"{price * 1.4:.2f}")
    elif item_type == "Accessories":
        if price <= 20.50 and price <= budget:
            profit += price * 0.4
            budget -= price
            sold_items.append(f"{price * 1.4:.2f}")

print(*sold_items)
print(f"Profit: {profit:.2f}")
if ticket:
    print("Hello, France!")
else:
    print("Not enough money.")




