nums = [int(x) for x in input().split(", ")]
positive = [int(x) for x in nums if x >= 0]
negative = [int(x) for x in nums if x < 0]
even = [int(x) for x in nums if x % 2 == 0]
odd = [int(x) for x in nums if not x % 2 == 0]

print(f"Positive: ", end = "")
print(*positive, sep = ", ")
print(f"Negative: ", end="")
print(*negative, sep = ", ")
print(f"Even: ", end = "")
print(*even, sep = ", ")
print(f"Odd: ", end = "")
print(*odd, sep = ", ")