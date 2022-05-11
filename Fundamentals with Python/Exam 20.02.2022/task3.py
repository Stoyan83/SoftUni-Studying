cards = input().split(", ")
number = int(input())

for num in range(number):
    command = input().split(", ")

    if command[0] == "Add":
        card = command[1]
        if card in cards:
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")

    elif command[0] == "Remove":
        card = command[1]
        if card not in cards:
            print("Card not found")
        else:
            cards.remove(card)
            print("Card successfully removed")
    elif command[0] == "Remove At":
        index = int(command[1])
        if index < 0 or index > len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")

    elif command[0] == "Insert":
        index = int(command[1])
        card = command[2]
        if index < 0 or index > len(cards):
            print("Index out of range")
        else:
            if card in cards:
                print("Card is already added")
            else:
                cards.insert(index, card)
                print("Card successfully added")

print(*cards, sep=", ")



