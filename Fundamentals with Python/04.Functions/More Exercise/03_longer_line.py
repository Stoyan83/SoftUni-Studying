def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)
    third_point = abs(x3) + abs(y3)
    forth_point = abs(x4) + abs(y4)
    first_line = first_point + second_point
    second_line = third_point + forth_point

    if first_line >= second_line:
        if first_point <= second_point:
            return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
        else:
            return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"
    else:
        if third_point <= forth_point:
            return f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})"
        else:
            return f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
