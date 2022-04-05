products = input().split()
searched = input().split()
stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = int(value)

for p in searched:
    if p in stock.keys():
        print(f"We have {stock[p]} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")



