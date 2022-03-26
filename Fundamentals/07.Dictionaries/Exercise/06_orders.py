data = input()

products = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    data = input()

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")

