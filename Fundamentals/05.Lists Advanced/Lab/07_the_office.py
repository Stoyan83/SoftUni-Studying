happiness = [int(x) for x in input().split()]
factor = int(input())

multiply_happ = [x * factor for x in happiness]

avg_happ = sum(multiply_happ) / len(multiply_happ)

final_happ = [x for x in multiply_happ if x >= avg_happ]


if len(final_happ) >= len(multiply_happ) / 2:
    print(f"Score: {len(final_happ)}/{len(multiply_happ)}. Employees are happy!")
else:
    print(f"Score: {len(final_happ)}/{len(multiply_happ)}. Employees are not happy!")
