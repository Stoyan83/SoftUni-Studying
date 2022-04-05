number_of_lines = int(input())
dict = {}

for pairs in range(0,number_of_lines):
    key = input()
    value = input()
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]

for key, value in dict.items():
    print(f"{key} - {', '.join(value)}")