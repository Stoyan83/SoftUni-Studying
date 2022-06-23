def start_spring(**kwargs):
    new_dict = {}
    result = ""
    for key, value in kwargs.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)
    sorted_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for k, v in sorted_dict:
        result += k + ":" + '\n'
        result += '-' + '\n-'.join(sorted(v))
        result += "\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
