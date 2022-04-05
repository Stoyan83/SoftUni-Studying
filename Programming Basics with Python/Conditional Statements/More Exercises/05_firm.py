from math import floor

hours_needed = int(input()) #99
days_available = int(input()) #3
employees = int(input()) #1

total_hours = floor((days_available * 8) * 0.90) + ((employees * 2) * days_available)

if total_hours >= hours_needed:
    hours_left = abs(hours_needed - total_hours)
    print(f"Yes!{hours_left} hours left.")

else:
    hours_not_enough = hours_needed - total_hours
    print(f"Not enough time!{hours_not_enough} hours needed.")