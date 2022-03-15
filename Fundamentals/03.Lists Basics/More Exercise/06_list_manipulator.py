import sys

list_input = [int(x) for x in input().split()]

command = input()

while not command == "end":
    current_command = command.split()

    if current_command[0] == "exchange":
        index = int(current_command[1])
        if index < 0 or index >= len(list_input):
            print("Invalid index")
        else:
            left = list_input[index + 1:]
            right = list_input[:index +1]
            list_input = left + right

    elif current_command[0] == "max":
        if current_command[1] == "even":
            if len([x for x in list_input if x % 2 == 0]) == 0:
                print("No matches")
            else:
                max_el_index = list_input[-1]
                max_num = -sys.maxsize
                for el in range(len(list_input) - 1, -1, -1):
                    if list_input[el] % 2 == 0:
                        if list_input[el] > max_num:
                            max_num = list_input[el]
                            max_el_index = el
                print(max_el_index)
        elif current_command[1] == "odd":
            if len([x for x in list_input if x % 2 != 0]) == 0:
                print("No matches")
            else:
                max_el_index = list_input[-1]
                max_num = -sys.maxsize
                for el in range(len(list_input) - 1, -1, -1):
                    if list_input[el] % 2 != 0:
                        if list_input[el] > max_num:
                            max_num = list_input[el]
                            max_el_index = el
                print(max_el_index)
    elif current_command[0] == "min":
        if current_command[1] == "even":
            if len([x for x in list_input if x % 2 == 0]) == 0:
                print("No matches")
            else:
                min_el_index = list_input[-1]
                min_num = sys.maxsize
                for el in range(len(list_input) - 1, -1, -1):
                    if list_input[el] % 2 == 0:
                        if list_input[el] < min_num:
                            min_num = list_input[el]
                            min_el_index = el
                print(min_el_index)
        if current_command[1] == "odd":
            if len([x for x in list_input if x % 2 != 0]) == 0:
                print("No matches")
            else:
                min_el_index = list_input[-1]
                min_num = sys.maxsize
                for el in range(len(list_input) - 1, -1, -1):
                    if list_input[el] % 2 != 0:
                        if list_input[el] < min_num:
                            min_num = list_input[el]
                            min_el_index = el
                print(min_el_index)

    elif current_command[0] == "first":
        count = int(current_command[1])
        if len(list_input) < count:
            print("Invalid count")
        else:
            if current_command[-1] == "even":
                new_list = list_input[:count]
                temp_list = [int(x) for x in new_list if x % 2 == 0]
                print(temp_list)
            elif current_command[-1] == "odd":
                new_list = list_input[:count]
                temp_list = [int(x) for x in new_list if x % 2 != 0]
                print(temp_list)
    elif current_command[0] == "last":
        count = int(current_command[1])
        if len(list_input) < count:
            print("Invalid count")
        else:
            if current_command[-1] == "even":
                new_list = list_input[(len(list_input)-count):len(list_input)]
                temp_list = [int(x) for x in new_list if x % 2 == 0]
                print(temp_list)
            elif current_command[-1] == "odd":
                new_list = list_input[(len(list_input) - count):len(list_input)]
                temp_list = [int(x) for x in new_list if x % 2 != 0]
                print(temp_list)


    command = input()

print(list_input)
