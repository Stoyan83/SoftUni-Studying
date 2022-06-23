sequence = input().split("|")
flatten_matrix = []

print(sequence)
for l in sequence[::-1]:
    flatten_matrix.append([int(x) for x in l.split()])

print(*sum(flatten_matrix, []))

