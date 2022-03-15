scripted_list = input()
decipher_text = ""

numbers_list = [int(x) for x in scripted_list if x.isdigit()]
char_list = [x for x in scripted_list if not x.isdigit()]
take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[j] for j in range(len(numbers_list)) if j % 2 != 0]

for k in range(len(take_list)):
    decipher_text += "".join(char_list[:take_list[k]])
    char_list = char_list[take_list[k] + skip_list[k]:]

print(decipher_text)

# 02.
# new_list = input()
#
# taken_string = ""
# skipped_string = ""
# numbers_list = [int(x) for x in new_list if x.isnumeric()]
# non_numbers_list = [x for x in new_list if not x.isnumeric()]
#
# for i in range(len(numbers_list)):
#     if i % 2 == 0:
#         taken_string += "".join(non_numbers_list[0:numbers_list[i]])
#         non_numbers_list = non_numbers_list[numbers_list[i]:]
#
#     else:
#         skipped_string += "".join(non_numbers_list[0:numbers_list[i]])
#         non_numbers_list = non_numbers_list[numbers_list[i]:]
#
# print(taken_string)
