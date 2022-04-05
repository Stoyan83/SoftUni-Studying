numbers =input().split()
text = [el for el in input()]
new_text = []


for num in numbers:
    total = 0
    for nums in num:
        total += int(nums)
        index = total
        if index > len(text):
            while index > len(text):
                 index -= len(text)

    new_text.append(text[index])
    text.pop(index)
print("".join(new_text))












