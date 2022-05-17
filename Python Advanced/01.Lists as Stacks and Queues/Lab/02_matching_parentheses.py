sequence_stack = list(input())
open_parenthesis = []

for ch in range(len(sequence_stack)):
    if sequence_stack[ch] == "(":

        open_parenthesis.append(ch)

    elif sequence_stack[ch] == ")":
        start_index = open_parenthesis.pop()

        print(*sequence_stack[start_index:ch + 1], sep="")
