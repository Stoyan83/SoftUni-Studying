def perfect_num(number):
    sum_num = []
    for num in range(1, number):
        if number % num == 0:
            sum_num.append(num)
    if sum(sum_num) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_num = int(input())
print(perfect_num(current_num))
