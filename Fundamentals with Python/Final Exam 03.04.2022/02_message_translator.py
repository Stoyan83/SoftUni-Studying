import re

number_of_lines = int(input())

pattern =r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]"



for i in  range(number_of_lines):
    line = input()
    match = re.match(pattern, line)
    if match:
       print(f"{match.group(1)}: {' '.join([str(ord(ch)) for ch in match.group(2)])}")
    else:
        print("The message is invalid")