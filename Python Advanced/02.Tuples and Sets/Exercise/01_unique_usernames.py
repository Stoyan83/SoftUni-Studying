n = int(input())

unique_usernames = set()

for _ in range(n):
    unique_usernames.add(input())

print(*unique_usernames, sep="\n")
