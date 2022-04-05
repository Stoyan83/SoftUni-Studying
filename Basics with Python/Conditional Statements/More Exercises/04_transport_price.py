km = int(input())
rate = input()

taxi_price_day = 0.70 + (km * 0.79)
taxi_price_night = 0.70 + (km * 0.90)
bus_price = 0.09 * km
train_price = 0.06 * km

if km < 20:

    if rate == "day":
        print(f"{taxi_price_day:.2f}")

    elif rate == "night":
        print(f"{taxi_price_night:.2f}")

elif km < 100:

    if rate == "day":

        if bus_price < taxi_price_day:
            print(f"{bus_price:.2f}")

        elif taxi_price_day < bus_price:
            print(f"{taxi_price_day:.2f}")

    if rate == "night":

        if bus_price < taxi_price_night:
            print(f"{bus_price:.2f}")

        elif taxi_price_night < bus_price:
            print(f"{taxi_price_night:.2f}")

else:
    print(f"{train_price:.2f}")