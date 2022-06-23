def rectangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a == 0 or b == 0:
        return "Enter valid values!"

    def area():
        return f"Rectangle area: {a * b}"

    def perimeter():
        return f"Rectangle perimeter: {2 * a + 2 * b}"


    return "\n".join([area(),perimeter()])



print(rectangle(2, 10))
print(rectangle('2', 10))




