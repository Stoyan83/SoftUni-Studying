def min_max_sum(numbers):
    nums = [int(x) for x in numbers.split()]
    return  f"The minimum number is {min(nums)}\nThe maximum " \
            f"number is {max(nums)}\nThe sum number is {sum(nums)}"

num = input()
print(min_max_sum(num))
