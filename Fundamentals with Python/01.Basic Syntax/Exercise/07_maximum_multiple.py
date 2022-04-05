devisor = int(input())
boundary = int(input())
list = []

for num in range(1, boundary + 1):
    if num % devisor == 0:
        list.append(num)

print(max(list))