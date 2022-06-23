def recursive_power(num, power=10):
    result = num
    if power > 1:
        result *= recursive_power(num, power - 1)

    return result


print(recursive_power(2, 10))
