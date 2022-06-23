def shopping_list(budget, **kwargs):
    result = ""
    products = set()
    current_budget = budget
    if budget < 100:
        return "You do not have enough budget."
    for i, p in kwargs.items():
        current_sum = p[0] * p[1]
        if current_budget >= current_sum:
            products.add(p)
            if len(products) > 5:
                break
            current_budget -= current_sum
            result += f"You bought {i} for {current_sum:.2f} leva.\n"

    return result

print(shopping_list(100))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
