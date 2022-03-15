integers_list = [int(x) for x in input().split(", ")]
temporary_list = []

boundary = 10
upper_boundary = 0
counter = 0

while len(integers_list) > counter:
    for number in integers_list:

        if upper_boundary < number <= boundary:
            temporary_list.append(number)
            counter += 1
            number = -1

    print(f"Group of {boundary}'s: {temporary_list}")

    temporary_list.clear()
    boundary += 10
#     upper_boundary += 10

# numbers = [int(el) for el in input().split(", ")]
# the_list = []
# max_element_in_numbers = max(numbers)
#
# for i in range(10, max_element_in_numbers + 10, 10):
#     the_list = list(filter((lambda x: i - 10 < x <= i), numbers))
#     print(f"Group of {i}'s: {the_list}")
#     the_list.clear()