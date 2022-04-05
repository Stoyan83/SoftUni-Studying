word = input().lower()

sand = word.count("sand")
water = word.count("water")
fish = word.count("fish")
sun = word.count("sun")

result = sand + water + fish + sun

print(result)