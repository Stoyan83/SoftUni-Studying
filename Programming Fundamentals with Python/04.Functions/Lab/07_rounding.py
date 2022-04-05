def rounding(numbers):
    result = [round(float(i)) for i in numbers.split()]
    return result


print(rounding(input()))
