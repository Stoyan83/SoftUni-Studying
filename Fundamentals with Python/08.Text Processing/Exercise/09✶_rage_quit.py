# string = input().upper() + " "
# current_sequence = ""
# final_sequence = ""
# unique_symbols = ""
#
# for i in range(len(string)):
#     if not string[i].isdigit():
#         current_sequence += string[i]
#
#     else:
#         if not string[i + 1].isdigit():
#             current_sequence *= int(string[i])
#             final_sequence += current_sequence
#             current_sequence = ""
#
#         elif string[i + 1].isdigit():
#             current_sequence *= int(string[i] + string[i + 1])
#             final_sequence += current_sequence
#             current_sequence = ""
#
# for j in final_sequence:
#     if j not in unique_symbols:
#         unique_symbols += j
#
# print(f"Unique symbols used: {len(unique_symbols)}")
# print(final_sequence)

line = input()
i = 0
rage_str = ""
result = ""


while i < len(line):
    ch = line[i]

    if ch.isdigit():
        count_str = ch

        if i + 1 < len(line) and line[i + 1].isdigit():
            count_str += line[i+1]
            i += 1

        count = int(count_str)
        result += rage_str.upper() * count

        rage_str = ""

    else:
        rage_str += ch

    i += 1

unique_count = len(set(result))
print(f"Unique symbols used: {unique_count}")
print(result)