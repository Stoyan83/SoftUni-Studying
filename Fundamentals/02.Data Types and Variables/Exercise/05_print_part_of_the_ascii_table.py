start_ascii = int(input())
stop_ascii = int(input())


for letter in range(start_ascii, stop_ascii + 1):
    print(chr(letter), end = " ")