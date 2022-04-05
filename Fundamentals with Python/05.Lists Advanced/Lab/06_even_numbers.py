numbers = [int(x) for x in input().split(", ")]
indices = []

for num in  range(len(numbers)):
    if numbers[num] % 2 == 0:
        indices.append(num)

print(indices)