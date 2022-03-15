loot = input().split(", ")
number_of_beggars = int(input())
final_loot = []
start = 0
sum_nums = 0

for beggar in range(number_of_beggars):
    for turn in range(start, len(loot), number_of_beggars):
        sum_nums += int(loot[turn])
    final_loot.append(sum_nums)

    sum_nums = 0
    start += 1

print(final_loot)