import re

letter_path = r'[a-z]'
punctuation_path = r"[',\.\!\?-]"


def get_n(line, path):
    return len(re.findall(path, line, re.IGNORECASE))


with open('text.txt', 'r') as file, open('output.txt', "w") as file1:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letters = get_n(line, letter_path)
        n_punctuation = get_n(line, punctuation_path)
        file1.writelines(f'Line {counter}: {line[:-1]} ({n_letters})({n_punctuation})\n')
        counter += 1
