import re

line = input()

pattern = r"(^|\b)[A-Z][a-z]+\s[A-Z][a-z]+(?:\b|$)"

matches = re.finditer(pattern, line)

for match in matches:
    print(match.group(), end=" ")