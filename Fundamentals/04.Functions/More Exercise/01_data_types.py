def data_types(command, number):
    if command == "int":
        result = int(number) * 2
    elif command == "real":
        result = f"{float(number) * 1.5:.2f}"

    elif command == "string":
        result = f"${number}$"

    return result


print(data_types(input(), input()))
