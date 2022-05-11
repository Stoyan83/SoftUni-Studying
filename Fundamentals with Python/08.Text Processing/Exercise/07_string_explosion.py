# text = [x for x in input()]
#
# power = 0
#
# for ch in range(len(text)):
#     if text[ch] == ">":
#         power += int(text[ch + 1])
#
#     else:
#         if power > 0:
#             text[ch] = " "
#             power -= 1
#
# text = [y for y in text if y != " "]
#
# print(*text, sep="")


text = input()
power = 0
new_text = ""

for index in range(len(text)):
    if text[index] != ">" and power > 0:
        power -= 1
    elif text[index] == ">":
        power += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)