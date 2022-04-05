annual_fee = int(input())

snickers = annual_fee - annual_fee * 0.4
team_uniform = snickers - snickers * 0.2
ball = team_uniform / 4
accessories = ball / 5

total_sum = annual_fee + snickers + team_uniform + ball + accessories

print(total_sum)
