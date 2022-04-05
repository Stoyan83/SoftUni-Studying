from math import floor

length = float(input())
width = float(input())

rows = floor((width - 1) / 0.70)
columns = floor(length / 1.2)
working_places = rows * columns - 3

print(working_places)
