def multiplication_sign(num1, num2, num3):

    result = [num1, num2, num3]
    negative = len([x for x in result if x < 0])
    zeroes = len([x for x in result if x == 0])

    if zeroes > 0:
        print('zero')
    elif negative == 1 or negative == 3:
        print('negative')
    else:
        print('positive')

multiplication_sign(int(input()),int(input()),int(input()))