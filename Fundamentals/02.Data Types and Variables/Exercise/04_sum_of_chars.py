number_of_lines = int(input())
numbers_to_sum = []

for nums in range(number_of_lines):
    letter = input()
    numbers_to_sum.append(int(ord(letter)))

print(f"The sum equals: {sum(numbers_to_sum)}")
