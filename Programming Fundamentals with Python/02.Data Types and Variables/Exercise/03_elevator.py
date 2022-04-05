from math import ceil

number_of_people = int(input())
capacity = int(input())

result = number_of_people / capacity

print(ceil(result))