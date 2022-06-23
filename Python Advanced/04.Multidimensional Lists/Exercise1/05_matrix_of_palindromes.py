# import string
# alphabet_dict = (zip(range(1, 27), string.ascii_lowercase))
# print(dict(alphabet_dict)) # -----take te print result as needed dictionary

alphabet_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10:
    'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20:
                     't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
                 }

row, column = [int(x) for x in input().split()]
matrix = []

for i in range(row):
    matrix_elements = []
    matrix.append(matrix_elements)
    for j in range(column):
        palindrome = f"{alphabet_dict[i + 1]}{alphabet_dict[i + 1 + j]}{alphabet_dict[i + 1]}"
        matrix_elements.append(palindrome)

for rows in matrix:
    print(*rows)
