number = int(input())

for letter1 in range(97,number + 97):
    for letter2 in range(97,number + 97):
        for letter3 in range(97,number + 97):
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}")
