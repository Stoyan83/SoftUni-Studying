number_key = int(input())
number_of_letters = int(input())
decrypted_word = ""

for letters in range(number_of_letters):
    letter = input()
    new_letter = ord(letter) + number_key
    decrypted_word += chr(new_letter)

print(decrypted_word)