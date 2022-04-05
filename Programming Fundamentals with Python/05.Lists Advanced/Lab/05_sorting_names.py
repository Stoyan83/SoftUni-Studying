# names = input().split(", ")

names_sorted = sorted(input().split(", "), key= lambda x: (-len(x), x))

print(names_sorted)