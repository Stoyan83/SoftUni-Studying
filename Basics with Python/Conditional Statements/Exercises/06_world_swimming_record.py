from math import floor


world_record = float(input())
distane = float(input())
time_per_meter = float(input())

time = distane * time_per_meter

delay = floor((distane / 15)) * 12.5

total_time = time + delay


difference_in_time = world_record - total_time

if world_record <= total_time:
    print(f"No, he failed! He was {abs(difference_in_time):.2f} seconds slower.")

else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
