def odd_even_sum(number):
  odd = 0
  even = 0
  for nums in number:
    if int(nums) % 2 == 0:
      even += int(nums)
    else:
      odd += int(nums)
  return f"Odd sum = {odd}, Even sum = {even}"

number = input()
print(odd_even_sum(number))