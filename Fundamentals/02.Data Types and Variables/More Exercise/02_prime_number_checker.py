# number = int(input())
#
# if number > 1 and number % 2 != 0 and number % 3 != 0 or number == 2 or number == 3:
#     print("True")
# else:
#     print("False")

number = int(input())

counter = 0

for i in range(2, number + 1):
    if number % i == 0:
        counter += 1
if counter == 1:
    print("True")
else:
    print("False")