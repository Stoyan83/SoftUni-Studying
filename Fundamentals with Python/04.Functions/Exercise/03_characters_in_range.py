def char_range(symbol1, symbol2):
    result = []
    for char in range(ord(symbol1) + 1, ord(symbol2)):
       result.append(chr(char))
    return " ".join(result)


symb1 = input()
symb2 = input()

print(char_range(symb1, symb2))