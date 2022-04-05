word = input()
new_word = []

for i in range(len(word)):
    if word[i].isupper():
        new_word.append(i)

print(new_word)


