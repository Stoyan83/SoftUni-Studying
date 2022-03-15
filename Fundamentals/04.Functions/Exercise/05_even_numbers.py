def even_numbers(number):
    nums = [int(x) for x in number.split() if int(x) % 2 == 0]
    return nums

numbers = input()
print(even_numbers(numbers))