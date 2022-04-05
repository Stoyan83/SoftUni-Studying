from math import ceil

holidays = int(input())

workdays = 365 - holidays
total_play_hours = (holidays * 127) + (workdays * 63)
difference = abs(30000 - total_play_hours)
hours = difference / 60
minutes = (hours - int(hours)) * 60

if total_play_hours > 30000:
    print("Tom will run away")
    print(f"{int(hours)} hours and {round(minutes)} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{(int(hours))} hours and {round(minutes)} minutes less for play")