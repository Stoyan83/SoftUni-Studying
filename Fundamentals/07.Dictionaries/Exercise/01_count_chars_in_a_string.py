text = input()

counter = {}

for char in text:
    if not char == " ":
        if not char in counter:
            counter[char] = 1
        else:
            counter[char] += 1


for key, value in counter.items():
    print(f"{key} -> {value}")




