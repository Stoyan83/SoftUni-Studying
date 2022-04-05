number = float(input())

if number == 0:
    print("zero")
if -1 > number >= -1000000:
    print("negative")
elif 0 > number >= -1:
    print("small negative")
elif number < -1000000:
    print("large negative")

if 1 < number <= 1000000:
    print("positive")
elif 0 < number <= 1:
    print("small positive")
elif number > 1000000:
    print("large positive")
