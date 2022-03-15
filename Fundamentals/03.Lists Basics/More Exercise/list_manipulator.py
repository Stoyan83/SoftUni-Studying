import sys


def exchange_list(list_input, index):
    if index >= len(list_input):
        print("Invalid index")
        return list_input
    elif index < 0:
        print("Invalid index")
        return list_input
    else:
        left_part = list_input[:index + 1]
        right_part = list_input[index + 1:]
        list_input = right_part + left_part
        return list_input


def max_even_odd(list_input):
    max_num_even = -sys.maxsize
    max_num_odd = -sys.maxsize
    for index in range(len(list_input)):
        if list_input[index] % 2 == 0:
            if list_input[index] >= max_num_even:
                max_num_even = list_input[index]
                max_num_even_index = index
        elif not list_input[index] % 2 == 0:
            if list_input[index] >= max_num_odd:
                max_num_odd = list_input[index]
                max_num_odd_index = index
    if current_command[-1] == "even":
        if max_num_even == -sys.maxsize:
            result = "No matches"
        else:
            result = max_num_even_index
        return result

    elif current_command[-1] == "odd":
        if max_num_odd == -sys.maxsize:
            result = "No matches"
        else:
            result = max_num_odd_index
        return result


def min_even_odd(list_input):
    min_even_num = sys.maxsize
    min_odd_num = sys.maxsize
    for index in range(len(list_input)):
        if list_input[index] % 2 == 0:
            if list_input[index] <= min_even_num:
                min_even_num = list_input[index]
                min_num_even_index = index
        elif not list_input[index] % 2 == 0:
            if list_input[index] <= min_odd_num:
                min_odd_num = list_input[index]
                min_num_odd_index = index
    if current_command[-1] == "even":
        if min_even_num == sys.maxsize:
            result = "No matches"
        else:
            result = min_num_even_index
        return result
    if current_command[-1] == "odd":
        if min_odd_num == sys.maxsize:
            result = "No matches"
        else:
            result = min_num_odd_index
        return result


def first_last_even_odd(list_input, index):
    if int(index) > len(list_input):
        return "Invalid count"
    even_list = []
    odd_list = []

    for i in range(len(list_input)):
        if list_input[i] % 2 == 0:
            even_list.append(list_input[i])
        if not list_input[i] % 2 == 0:
            odd_list.append(list_input[i])
    if current_command[0] == "first":
        if current_command[-1] == "even":
            result = even_list[:index]
        else:
            result = odd_list[:index]
        return result
    elif current_command[0] == "last":
        if current_command[-1] == "even":
            result = even_list[-index:]
        else:
            result = odd_list[-index:]
        return result


list_input = [int(el) for el in input().split()]

command = input()

while not command == "end":
    current_command = command.split()

    if current_command[0] == "exchange":
        list_input = exchange_list(list_input, int(current_command[-1]))

    elif current_command[0] == "max":
        print(max_even_odd(list_input))

    elif current_command[0] == "min":
        print(min_even_odd(list_input))

    elif current_command[0] == "first" or current_command[0] == "last":
        print(first_last_even_odd(list_input, int(current_command[1])))

    command = input()

print(list_input)
