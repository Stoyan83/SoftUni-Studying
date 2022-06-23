from collections import deque

searched_words = [["r", "o", "s", "e"],
                  ["t", "u", "l", "i", "p"],
                  ["l", "o", "t", "u", "s"],
                  ["d", "a", "f", "f", "o", "d", "i", "l"]]

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]
found = False
searched = ""

while True:
    if not vowels or not consonants:
        break
    if found:
        break
    searched_vowel = vowels.popleft()

    searched_consonant = consonants.pop()
    for r in range(len(searched_words)):
        if found:
            break

        for c in range(len(searched_words[r])):
            if searched_words[r][c] == searched_vowel:
                searched_words[r][c] = searched_words[r][c].upper()

            elif searched_words[r][c] == searched_consonant:
                searched_words[r][c] = searched_words[r][c].upper()

            if "".join(searched_words[r]).isupper():
                searched = "".join(searched_words[r]).lower()
                found = True
                break

if found:
    print(f"Word found: {searched}")
else:
    print("Cannot find any word!")

if vowels:
    print("Vowels left: ", end="")
    print(*vowels, sep=" ")
if consonants:
    print("Consonants left: ", end="")
    print(*consonants, sep=" ")

# Other author solution
#
# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
# words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
# found_word = False
#
# while vowels and consonants:
#     v = vowels.popleft()
#     c = consonants.pop()
#     for word in words.keys():
#         words[word] = words[word].replace(v, '')
#         words[word] = words[word].replace(c, '')
#         if words[word] == '':
#             print(f"Word found: {word}")
#             found_word = True
#             break
#     if found_word:
#         break
#
# if not found_word:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")
#
