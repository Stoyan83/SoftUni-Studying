number = int(input())
even = []
odd = []
negative = []
positive = []

for num in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number < 0:
        negative.append(current_number)
    else:
        positive.append(current_number)

command = input()

# if command == "even":
#     print(even)
# elif command == "odd":
#     print(odd)
# elif command == "negative":
#     print(negative)
# elif command == "positive":
#

print(eval(command))

