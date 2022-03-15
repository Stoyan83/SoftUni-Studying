first_line_str = input()
second_line_str = input()
third_line_str = input()

str_to_lst_1line = first_line_str.split()
str_to_lst_2line = second_line_str.split()
str_to_lst_3line = third_line_str.split()
combine_list = str_to_lst_1line + str_to_lst_2line + str_to_lst_3line



axes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
first_player_won = any(combine_list[a] + combine_list[b] + combine_list[c] in ["111"] for a, b, c in axes)
second_player_won = any(combine_list[a] + combine_list[b] + combine_list[c] in ["222"] for a, b, c in axes)



if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")