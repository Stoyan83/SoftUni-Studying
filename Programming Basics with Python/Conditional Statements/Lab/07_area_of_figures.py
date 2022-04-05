from math import pi

shape = str(input())


if shape == "square":
    a = float(input())
    s = a * a

elif shape == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b

elif shape == "circle":
    r = float(input())
    s = pi * (r ** 2)


elif shape == "triangle":
    a = float(input())
    b = float(input())
    s = (a * b) / 2

print(f"{s:.3f}")