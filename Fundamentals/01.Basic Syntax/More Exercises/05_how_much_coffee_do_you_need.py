coffee = 0
need_sleep = False

command = input()
while command != "END":

    if command == "dog" or command == "cat" or command == "coding" \
            or command == "movie":
        coffee += 1

    elif command == "DOG" or command == "CAT" or command == "CODING" \
            or command == "MOVIE":
        coffee += 2

    if coffee > 5:
        need_sleep = True
        break

    command = input()

if need_sleep:
    print("You need extra sleep")

else:
    print(coffee)