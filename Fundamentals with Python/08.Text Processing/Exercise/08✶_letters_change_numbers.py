def letter_position(letter):
    position = ord(letter.lower()) - 96
    return position


number = ""
result = 0
final_res = 0
f
text = input().split()

for word in text:
    for ch in word:
        if ch.isdigit():
            number += ch

    if word[0].isupper():
        result = int(number) / letter_position(word[0])

    else:
        result = int(number) * letter_position(word[0])

    if word[-1].isupper():
        result -= letter_position(word[-1])

    else:
        result += letter_position(word[-1])

    final_res += result
    result = 0
    number = ""

print(f"{final_res:.2f}")

#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# char_num = lambda x: alphabet.find(x.lower()) + 1
#
# input_strings  = [x for x in input().split()]
# output = 0
#
# for word in input_strings:
#     first_char_num = char_num(word[0])
#     last_char_num = char_num(word[-1])
#     number_in_word = int(word[1:-1])
#
#     if word[0].isupper():
#         number_in_word /= first_char_num
#     elif word[0].islower():
#         number_in_word *= first_char_num
#
#     if word[-1].isupper():
#         number_in_word -= last_char_num
#     elif word[-1].islower():
#         number_in_word += last_char_num
#
#     output += number_in_word
#
# print(f"{output:.2f}")