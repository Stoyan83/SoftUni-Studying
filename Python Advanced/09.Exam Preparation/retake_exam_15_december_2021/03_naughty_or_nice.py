from collections import Counter


def naughty_or_nice_list(names_list, *args, **kwargs):
    kids_dict = {"Nice": [], "Naughty": [], "Not found": []}
    counter = Counter(el[0] for el in names_list)


    for i in args:
        number, behavior = i.split("-")
        number = int(number)
        if counter[number] == 1:
            name = [name for num, name in names_list if num == number]
            kids_dict[behavior].extend(name)
            names_list = [el for el in names_list if el[0] != number]
    name_counter = Counter(el[1] for el in names_list)

    for name, type in kwargs.items():
        if name_counter[name] == 1:
            kids_dict[type].append(name)
            names_list = [el for el in names_list if el[1] != name]

    for num, name in names_list:
        kids_dict["Not found"].append(name)

    output = ""

    for type, kids in kids_dict.items():
        if kids:
            output += f"{type}: {', '.join(kids)}\n"

    return output


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),

    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
