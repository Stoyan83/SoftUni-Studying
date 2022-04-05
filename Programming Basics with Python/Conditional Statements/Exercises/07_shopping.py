budget  = float(input())
video_card = int(input())
processors = int(input())
ram = int (input())

video_card_price = video_card * 250
processors_price = processors * video_card_price * 0.35
ram_price = ram * video_card_price * 0.1

price = video_card_price + processors_price + ram_price

if video_card > processors:
    price = price - (price * 0.15)

money_left = budget - price

if price <= budget:
    print(f"You have {abs(money_left):.2f} leva left!")

else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva more!")