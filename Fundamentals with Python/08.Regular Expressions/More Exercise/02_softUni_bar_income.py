import re

sum_products = []
pattern = r"%([A-Z]{1}[a-z]+)%<([\w\d]+)>[\w\d]*?\|(\d+)\|[a-zA-Z]*?(\d+.?\d*?)\$"
pattern1 = r"^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?)(?=\$)\$$"
p2 = r"^%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?([-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)\$"

while True:
    line = input()
    if line == "end of shift":
        break

    matches = re.finditer(pattern1, line)
    total = 0
    for m in matches:
        sum_products.append(int(m.group(3)) * float(m.group(4)))
        print(f"{m.group(1)}: {m.group(2)} - {int(m.group(3)) * float(m.group(4)):.2f}")

print(f"Total income: {sum(sum_products):.2f}")
