factor = int(input())
count = int(input())
number = []

for num in range(1, count + 1):
    number.append(num * factor)

print(number)