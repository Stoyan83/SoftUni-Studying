from math import floor

hour = int(input())
minutes = int(input())

hour_in_minutes = hour * 60

total_time = hour_in_minutes + minutes
time_after_15min = total_time + 15

hour_after = time_after_15min / 60
minutes_after = time_after_15min % 60



if floor(hour_after) == 24:
    print(f"0:{minutes_after:02d}")

else:
    print(f"{floor(hour_after)}:{minutes_after:02d}")