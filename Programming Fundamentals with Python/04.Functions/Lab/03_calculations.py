def calculate(operator, num1, num2):
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2

    return result


print(calculate(operator = input(), num1 = int(input()), num2 = int(input())))

