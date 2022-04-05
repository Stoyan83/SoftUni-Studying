def total_price(product, quantity):
    products = {"coffee": 1.5, "water": 1, "coke": 1.4, "snacks": 2}
    result = products[product] * quantity
    return f"{result:.2f}"

print(total_price(input(), int(input())))

