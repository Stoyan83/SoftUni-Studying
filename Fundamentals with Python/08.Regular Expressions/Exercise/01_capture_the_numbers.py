import re

pattern = re.compile(r"\d+")

line = input()
while True:
    if line:
        match = pattern.findall(line)
        if match:
            print(' '.join(match), end = " ")
        line = input()
    else:
        break


