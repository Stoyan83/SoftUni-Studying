n = int(input())
elements = set()

for _ in range(n):
    element = input().split()
    for i in element:
        elements.add(i)

print(*elements, sep="\n")
