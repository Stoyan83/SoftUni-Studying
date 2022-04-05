def palindrome(numbers):
    for i in numbers:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


nums = input().split(", ")
palindrome(nums)
