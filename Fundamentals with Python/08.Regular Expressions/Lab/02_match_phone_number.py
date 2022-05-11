import re

line = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

matches = re.finditer(pattern, line)

phones = []
for match in matches:
    phones.append(match.group())

print(*phones, sep=", ")

