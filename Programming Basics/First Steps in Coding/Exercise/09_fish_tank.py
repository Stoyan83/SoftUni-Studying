length = int(input())
width = int(input())
hight = int(input())
percentage = float(input())

volume = length * width * hight
volume_liters = volume / 1000

liters_needed = volume_liters - (volume_liters * percentage/100)

print(liters_needed)
