from math import ceil

tv_show = input()
show_duration = int(input())
lunchbreak = int(input())


lunch_time = lunchbreak / 8
rest = lunchbreak / 4

time_left = lunchbreak - (lunch_time + rest)



if time_left >= show_duration:
    print(f"You have enough time to watch {tv_show} and left with {(ceil(time_left - show_duration))} minutes free time.")

else:
    print(f"You don't have enough time to watch {tv_show}, you need {(ceil(show_duration - time_left))} more minutes.")