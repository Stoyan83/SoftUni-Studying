sequence = [int(x) for x in input().split()]
target_number = int(input())
pairs = []
count = 0

for i in range(len(sequence)):
    for j in range(i + 1, len(sequence)):
        count += 1
        if sequence[i] + sequence[j] == target_number:
            pairs.append((sequence[i], sequence[j]))
            print(f"{sequence[i]} + {sequence[j]} = {target_number}")

res = dict.fromkeys(pairs)

print(f"Iterations done: {count}")
for keys in res:
    print(keys)
