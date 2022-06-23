def list_manipulator(numbers, com1, com2, *args):
    if com1 == "remove":
        if com2 == "beginning":
            if args:
                numbers = numbers[args[0]:]
            else:
                numbers.pop(0)
        elif com2 == "end":
            if args:
                numbers = numbers[:len(numbers) - args[0]]
            else:
                numbers.pop()
    if com1 == "add":
        if com2 == "beginning":
            for i in range(len(args) - 1, -1, -1):
                numbers.insert(0, args[i])
        else:
            for j in range(len(args)):
                numbers.append(args[j])

    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
