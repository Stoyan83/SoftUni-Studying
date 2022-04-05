def sort_numbers(number):
    filtered = [int(x) for x in number.split()]
    filtered.sort()
    return filtered

nums = input()
print(sort_numbers(nums))