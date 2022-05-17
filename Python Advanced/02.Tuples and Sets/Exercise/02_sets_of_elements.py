n, m = input().split()
n = int(n)
m = int(m)
first = set()
second = set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

result = first.intersection(second)
print(*result, sep="\n")