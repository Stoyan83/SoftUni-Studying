from collections import deque

bows_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while True:
    if not bows_of_ramen or not customers:
        break

    if bows_of_ramen[-1] <= customers[0]:
        customers[0] -= bows_of_ramen[-1]
        bows_of_ramen.pop()
        if customers[0] <= 0:
            customers.popleft()
    elif bows_of_ramen[-1] >= customers[0]:
        bows_of_ramen[-1] -= customers[0]
        customers.popleft()
        if bows_of_ramen[-1] <= 0:
            bows_of_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bows_of_ramen:
        print("Bowls of ramen left: ", end="")
        print(*bows_of_ramen, sep=", ")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: ", end="")
    print(*customers, sep=", ")
