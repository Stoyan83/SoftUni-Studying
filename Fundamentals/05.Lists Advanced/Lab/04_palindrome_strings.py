text = input().split()
palindrome = input()
palindromes = [x for x in text if x == x[::-1]]

#
# for word in text:
#     if word == word[::-1]:
#         palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")


