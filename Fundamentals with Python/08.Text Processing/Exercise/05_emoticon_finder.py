text = input()

for n in range(len(text)- 1):
    if text[n] == ":" and not text == " ":
        print(f":{text[n + 1]}")


