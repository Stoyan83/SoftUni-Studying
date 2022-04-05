list_of_strings = input().split(" ")

new_words = ""
numbers = ""
letters = ""

for words in list_of_strings:
    for chars in words:
        if chars.isdigit():
            numbers += chars
        else:
            letters += chars

    new_words += (chr(int(numbers)))
    letters = list(letters)
    letters[0], letters[-1] = letters[-1], letters[0]
    letters = "".join(letters)
    new_words += letters
    numbers = ""
    letters = ""
    new_words += " "

print(new_words)