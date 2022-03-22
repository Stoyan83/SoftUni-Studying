from collections import Counter

text = input().lower().split()
for key,value in Counter(text).items():
    if value %  2 != 0:
        print(key, end=" ")
