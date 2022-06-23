def even_odd_filter(**kwargs):
    new_dict = {}
    sorted_kwargs = sorted(kwargs.items(), key = lambda x: (-len(x[1])))
    for key, value in sorted_kwargs:
        if key == 'even':
            value = [int(x) for x in value if x % 2 == 0]
        if key == 'odd':
            value = [int(x) for x in value if x % 2 != 0]
        new_dict[key] = value

    return new_dict

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
