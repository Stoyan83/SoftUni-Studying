circle = input().split()
step = int(input())
new_circle = []
counter = 0

while not len(circle) == 0:

    for i in range(len(circle)):
        counter += 1

        if counter % step == 0:
            new_circle.append(circle[i])
            circle[i] = None

    circle = [el for el in circle if el]

    new_circle = [int(el) for el in new_circle]
print(str(new_circle).replace(" ", ""))
