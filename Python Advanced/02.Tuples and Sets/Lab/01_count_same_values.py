nums = (float(el) for el in input().split())
counts = {}

for num in nums:
    if num not in counts:
        counts[num] = 0
    counts[num] += 1

for key, value in counts.items():
    print(f"{key} - {value} times")
