# number = int(input())
# counter = 0
#
# for _ in range(number):
#     symbol = input()
#     if symbol == "(":
#         counter += 1
#     if symbol == ")" and not counter == 1 or counter == 2:
#         result = "UNBALANCED"
#         break
#     if symbol == ")" and counter == 1:
#         result = "BALANCED"
#         counter = 0
#
# if counter == 1:
#     print("BALANCED")
# else:
#     print(result)

number = int(input())

last_bracket = ")"
balance = True
for _ in range(number):
    command = input()
    if command == "(" or command == ")":
        if not command == last_bracket:
            last_bracket = command
        else:
            balance = False

if balance:
    print("BALANCED")
else:
    print("UNBALANCED")