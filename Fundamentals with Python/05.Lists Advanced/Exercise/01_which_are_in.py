# first_list = input().split(", ")
# second_line = input().replace(", ","")
#
# new_list = [i for i in first_list if i in second_line]
#
# print(new_list)

first_list = input().split(", ")
second_list = input().split(", ")
new = []

for i in first_list:
    for j in second_list:
        if i in j:
            if i not in new:
                new.append(i)
print(new)
