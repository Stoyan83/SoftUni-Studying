def draw_figure(n):
    if n == 0:
        return

    print('*' * n)
    draw_figure(n - 1)
    print('#' * n)


draw_figure(int(input()))
