from collections import deque

numbers = deque()

string_of_numbers = input().split()

for ch in string_of_numbers:
    if ch not in "*+-/":
        numbers.append(int(ch))
    else:
        if ch == "/":
            ch = "//"
        result = ""
        while numbers:
            result += str(numbers.popleft())
            if len(numbers) > 0:
                result += ch
        result = eval(result)
        numbers.append(str(result))
        result = ""

print(*numbers)
