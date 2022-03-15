numbers = [int(el) for el in input().split()]
number_count = int(input())

for num in range(number_count):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")
