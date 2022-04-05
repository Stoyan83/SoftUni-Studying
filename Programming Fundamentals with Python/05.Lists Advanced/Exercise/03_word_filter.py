some_text = input().split()
even_text = list()

for words in some_text:
    if len(words) % 2 == 0:
        even_text.append(words)

for text in even_text:
    print(text)