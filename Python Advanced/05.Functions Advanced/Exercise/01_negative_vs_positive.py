def negative_positive(*args):
    result_positive = 0
    result_negative = 0
    for n in args:
        if n > 0:
            result_positive += n
        elif n < 0:
            result_negative += n

    print(result_negative)
    print(result_positive)
    if abs(result_negative) > result_positive:
        print("The negatives are stronger than the positives")
    if abs(result_negative) < result_positive:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
negative_positive(*numbers)
