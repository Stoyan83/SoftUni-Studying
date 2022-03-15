number = int(input())
positive = 0
negative_list = []
positive_list = []

for num in range(number):
    current_number = int(input())
    if current_number < 0:
        negative_list.append(current_number)
    else:
        positive_list.append(current_number)
        positive += 1

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive}")
print(f"Sum of negatives: {sum(negative_list)}")
