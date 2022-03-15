def factorial_dev(num1, num2):
    f1 = 1
    f2 = 1
    for i in range(num1, 1, -1):
        f1 *= i
    for j in range(num2, 1, -1):
        f2 *= j
    return f"{f1 / f2:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_dev(first_number, second_number))
