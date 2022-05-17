def ascii_sum(name):
    sum = 0
    for ch in name:
        sum += ord(ch)

    return sum


odd = set()
even = set()

n = int(input())

for i in range(n):
    current_name = ascii_sum(input()) // (i + 1)
    if current_name % 2 == 0:
        even.add(current_name)
    else:
        odd.add(current_name)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
else:
    print(*odd.symmetric_difference(even), sep=', ')
