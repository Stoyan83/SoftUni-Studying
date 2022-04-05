number_of_snowballs = int(input())
best_value = 0
best_weight_of_snowball = 0
best_time = 0
best_quality = 0


for balls in range(1, number_of_snowballs +1):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    value = int((weight_of_snowball / time_needed )** quality)
    if value > best_value:
        best_value = value
        best_weight_of_snowball = weight_of_snowball
        best_time = time_needed
        best_quality = quality


print(f"{best_weight_of_snowball} : {best_time} = {best_value} ({best_quality})")

