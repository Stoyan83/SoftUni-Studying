def words_sorting(*args):
    words_dict = {}
    result = ""
    for word in args:
        words_dict[word] = sum([ord(x) for x in word])

    if sum(words_dict.values()) % 2 == 1:
        odd_dict = sorted(words_dict.items(), key=lambda x: -x[1])
        for k, v in odd_dict:
            result += f"{k} - {v}\n"
        return result
    else:
        even_dict = sorted(words_dict.items())
        for k, v in even_dict:
            result += f"{k} - {v}\n"
        return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
