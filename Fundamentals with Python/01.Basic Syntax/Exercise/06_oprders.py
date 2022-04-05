number_of_orders = int(input())

total = 0

for nums in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    curent_price = price_per_capsule * days * capsules_count
    total += price_per_capsule * days * capsules_count
    print(f"The price for the coffee is: ${curent_price:.2f}")

print(f"Total: ${total:.2f}")


