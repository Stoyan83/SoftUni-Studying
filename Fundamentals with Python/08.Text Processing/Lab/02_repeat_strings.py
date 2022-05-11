text = input().split()
result = ""
for words in text:
   result += words * len(words)

print(result)