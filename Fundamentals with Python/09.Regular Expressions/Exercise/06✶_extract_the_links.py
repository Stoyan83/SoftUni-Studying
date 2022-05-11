import re

line = input()
valid_urls = []
pattern = r"((www\.)([a-zA-Z0-9]+[a-zA-Z0-9\-]+?[a-zA-Z0-9]+?\b)(\.[a-z]+)+)"
while line:
    matches = re.finditer(pattern, line)
    for match in matches:
        valid_urls.append(match.group(1))

    line = input()

for valid_url in valid_urls:
    print(valid_url)
