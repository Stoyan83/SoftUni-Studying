cards = input().split()
shuffles = int(input())

deck_half = len(cards) // 2

for i in range(1, shuffles + 1):

    left_part = cards[:deck_half]
    right_part = cards[deck_half:]
    cards = left_part + right_part

    new_list = []

    for j in range(len(left_part)):
        new_list.append(left_part[j])
        new_list.append(right_part[j])

    cards = new_list

print(cards)