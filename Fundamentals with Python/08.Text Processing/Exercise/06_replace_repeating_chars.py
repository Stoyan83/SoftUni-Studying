text = input()
new_text = ""
last_ch = ""

for ch in text:
    if not ch == last_ch:
        new_text += ch
        last_ch = ch

print(new_text)
