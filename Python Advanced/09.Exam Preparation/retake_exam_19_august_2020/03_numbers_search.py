def numbers_searching(*args):
    l1 = []
    l2 = []
    for i in args:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)

    missing = [x for x in range(min(l1), max(l1)) if x not in l1]
    missing.append(sorted(list(set((l2)))))
    return missing




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
