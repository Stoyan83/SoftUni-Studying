# def tribonacci_sequence(number):
#   tribonacci_list = [1]
#   tribonacci_sum = 1
#   tribonacci_last_three = []
#   for tribo in range(1, int(num)):
#     if tribo > 2:
#       tribonacci_sum = sum(tribonacci_list[-3:])
#       tribonacci_list.append(tribonacci_sum)
#     else:
#       tribonacci_sum = sum(tribonacci_list[:3])
#       tribonacci_list.append(tribonacci_sum)
#   print_string = " ".join(str(n) for n in tribonacci_list)
#   return print_string
#
#
# num = input()
#
# print(tribonacci_sequence(num))

number = int(input())

tribonacci_sequence = [0] * number
tribonacci_sequence[0] = 1

for index in range(1, len(tribonacci_sequence)):
    if index < 4:
        tribonacci_sequence[index] = sum(tribonacci_sequence)
    else:
        tribonacci_sequence[index] = sum(tribonacci_sequence[index - 3:index])

print(*tribonacci_sequence)