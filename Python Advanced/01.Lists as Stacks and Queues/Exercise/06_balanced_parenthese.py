parenthesis = list(input())
open_parenthesis = []
balanced = True

for i in range(len(parenthesis)):
    if parenthesis[i] in "{[(":
        open_parenthesis.append(parenthesis[i])
    else:
        if not open_parenthesis:
            balanced = False
            break
        open_p = open_parenthesis.pop()
        if open_p + parenthesis[i] not in "(){}[]":
            balanced = False
            break

if balanced and not open_parenthesis:
    print("YES")
else:
    print("NO")
