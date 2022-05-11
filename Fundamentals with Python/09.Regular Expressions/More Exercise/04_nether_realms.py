import re


def sum_health(demon):

    pattern =r"([-]?\d+(\.\d+)?)"
    damage = []

    matches = re.finditer(pattern, demon)

    for m in matches:
        damage.append(float(m.group()))

    return sum(damage)


def sum_multiply_devide(demon):
    total = 1
    for ch in demon:
        if ch == "*":
            total *= 2
        if ch == "/":
            total = total / 2

    return total


def damage_demon(demon):
    return sum_health(demon) * sum_multiply_devide(demon)


def health(demon):
    pattern1 = r"[^0-9\.\+\*\/\-]"
    health = 0
    health_symbols = re.findall(pattern1, demon)
    for symbol in health_symbols:
        health += ord(symbol)
    return health


demons = sorted([demon.strip() for demon in input().split(",")])

for d in demons:
    print(f"{d} - {health(d)} health, {damage_demon(d):.2f} damage")