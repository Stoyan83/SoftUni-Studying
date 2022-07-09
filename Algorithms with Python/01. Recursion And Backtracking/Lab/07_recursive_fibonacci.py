def fib(num):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(num - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


print(fib(int(input())))