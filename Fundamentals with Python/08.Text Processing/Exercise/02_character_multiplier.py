# text = input().split()
#
# shortest = min(len(text[0]), len(text[1]))
# total_sum = 0
#
# for n in range(shortest):
#     total_sum += ord(text[0][n]) * ord(text[1][n])
#
# text[0] = text[0][shortest:]
# text[1] = text[1][shortest:]
# text = "".join(text)
#
# for char in text:
#     total_sum += ord(char)
#
# print(total_sum)

def sum_multiplication(first, second):
    total = 0
    for index in range(min(len(first), len(second))):
        total += ord(first[index]) * ord(second[index])
    return total


def add_of_reminder(first, second):
    diff = abs(len(first) - len(second))
    if len(first) > len(second):
        return sum([ord(ch) for ch in first[-diff:]])
    elif len(second) > len(first):
        return sum([ord(ch) for ch in second[-diff:]])
    else:
        return 0


def total_sum(first, second):
    return sum_multiplication(first, second) + add_of_reminder(first, second)


text = input().split()
result = total_sum(text[0], text[1])
print(result)
