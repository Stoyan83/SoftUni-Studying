text = input().split(", ")
dict = {}

for letter in range(len(text)):
    key = text[letter]
    value = ord(text[letter])
    dict[key] = value


print(dict)