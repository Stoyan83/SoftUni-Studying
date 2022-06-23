def age_assignment(*args, **kwargs):
    result = ''
    sorted_args = sorted(args)
    for i in sorted_args:
        for j in kwargs:
            pass
        result +=  f"\n{i} is {kwargs.get(f'{i[0]}')} years old."

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
