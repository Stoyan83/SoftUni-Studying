def fill_the_box(*args):
    size = 1
    current_size = 0

    for n in args[:3]:
        size *= n

    for n in args[3:]:
        if str(n).isdigit():
            current_size += n
        else:
            break

    if size - current_size > 0:
        return f"There is free space in the box. You could put {size - current_size} more cubes."
    else:
        return f"No more free space! You have {abs(size - current_size)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
