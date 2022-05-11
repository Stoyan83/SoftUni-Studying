import re

line = input()

title_pattern = r'<title>(.+)<\/title>'
title = ''.join(re.findall(title_pattern, line))

body_pattern = r'<body>.+<\/body>'
body = ''.join(re.findall(body_pattern, line))

valid_body_content_pattern = r'>([^><]*)<'
valid_body = ''.join(re.findall(valid_body_content_pattern, body)).replace('\\n', '')

print(f'Title: {title}')
print(f'Content: {valid_body}')