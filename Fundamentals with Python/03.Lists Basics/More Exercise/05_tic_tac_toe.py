first_list = input().split()
second_list = input().split()
third_list = input().split()
draw = False

if first_list[0] == "1" and second_list[0] == "1" and third_list[0] == "1":
    winner = "First player"
elif first_list[1] == "1" and second_list[1] == "1" and third_list[1] == "1":
    winner = "First player"
elif first_list[2] == "1" and second_list[2] == "1" and third_list[2] == "1":
    winner = "First player"
elif first_list.count("1") == 3:
    winner = "First player"
elif second_list.count("1") == 3:
    winner = "First player"
elif third_list.count("1") == 3:
    winner = "First player"
elif first_list[0] == "1" and second_list[1] == "1" and third_list[2] == "1":
    winner = "First player"
elif first_list[2] == "1" and second_list[1] == "1" and third_list[0] == "1":
    winner = "First player"

elif first_list[0] == "2" and second_list[0] == "2" and third_list[0] == "2":
    winner = "Second player"
elif first_list[1] == "2" and second_list[1] == "2" and third_list[1] == "2":
    winner = "Second player"
elif first_list[2] == "2" and second_list[2] == "2" and third_list[2] == "2":
    winner = "Second player"
elif first_list.count("2") == 3:
    winner = "Second player"
elif second_list.count("2") == 3:
    winner = "Second player"
elif third_list.count("2") == 3:
    winner = "Second player"
elif first_list[0] == "2" and second_list[1] == "2" and third_list[2] == "2":
    winner = "Second player"
elif first_list[2] == "2" and second_list[1] == "2" and third_list[0] == "2":
    winner = "Second player"

else:
    print("Draw!")
    draw = True

if not draw:
    print(f"{winner} won")
