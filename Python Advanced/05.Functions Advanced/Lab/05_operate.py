# def operate(operator, *args):
#     result = args[0]
#
#     action = {
#         '+': lambda a, b: a + b,
#         '-': lambda a, b: a - b,
#         '*': lambda a, b: a * b,
#         '/': lambda a, b: a / b if b != 0 else a
#     }
#
#     for n in args[1:]:
#         result = action[operator](result, n)
#
#     return result
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

from functools import reduce

def operate(operator, *args):
    result = reduce(lambda x, y: eval(f"{x}{operator}{y}") if y != 0 else x, args)
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

