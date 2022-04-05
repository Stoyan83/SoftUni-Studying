def absolute_value(numbers):
    absolute_numbers = [abs(float(x)) for x in numbers.split()]
    return absolute_numbers


print(absolute_value(input()))