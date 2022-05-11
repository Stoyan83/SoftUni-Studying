import re

line = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, line)
print(*matches, sep=",")