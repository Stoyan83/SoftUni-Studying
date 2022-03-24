from math import floor

def center_point(x1, y1, x2, y2):
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)

    if first_point > second_point:
        return f"({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x1)}, {floor(y1)})"


print(center_point(float(input()), float(input()),float(input()),float(input())))

