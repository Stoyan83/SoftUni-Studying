data = input().split()
products = {}

for el in range(0, len(data), 2):
    key = data[el]
    value = data[el+1]
    products[key] = int(value)

print(products)
