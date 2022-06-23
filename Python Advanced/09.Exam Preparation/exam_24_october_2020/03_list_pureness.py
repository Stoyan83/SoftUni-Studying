from collections import deque


def best_list_pureness(list, k):

    best_result = 0
    current_list = deque(list)
    best_rotation = 0
    for i in range(0, k + 1):
        if i > 0:
            current_list.appendleft(current_list.pop())

        result = 0
        for index, value in enumerate(current_list):
            result += (index * value)
        if result > best_result:
            best_result = result
            best_rotation = i

    return f"Best pureness {best_result} after {best_rotation} rotations"



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
