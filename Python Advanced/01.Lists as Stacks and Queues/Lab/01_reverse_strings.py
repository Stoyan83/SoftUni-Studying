# from time import strftime
# from time import gmtime
#
# a = strftime("%H:%M:%S", gmtime(10000000000))

sequence_stack = list(input())

for _ in range(len(sequence_stack)):
    print(sequence_stack.pop(), end = "")
