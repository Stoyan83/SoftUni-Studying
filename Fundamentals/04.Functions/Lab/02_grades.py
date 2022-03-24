def grade(number):
    if 2 <= number < 3:
        result = "Fail"
    elif 3 <= number < 3.5:
        result = "Poor"
    elif 3.5 <= number < 4.5:
        result = "Good"
    elif 4.5 <= number < 5.5:
        result = "Very Good"
    elif 5.5 <= number <= 6:
        result = "Excellent"

    return result


print(grade(float(input())))