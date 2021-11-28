deposit_sum = float(input())
deposit_time = int(input())
annual_interest_rate = float(input())

total_sum = deposit_sum + deposit_time * ((deposit_sum * annual_interest_rate/100)/12)

print(total_sum)
