text = input()
new_text = ""

for ch in text:
    new_text += chr(ord(ch) + 3)

print(new_text)