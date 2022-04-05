from statistics import mean

pair_of_rows = int(input())

students = {}

for pair in range(pair_of_rows):
    name, grade = input(), float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

    #     students[name] = [grade]
    # else:
    #     students[name].append(grade)

for key, value in students.items():
    result = mean(value)
    # result = sum(value) / len(value)
    if result >= 4.5:
        print(f"{key} -> {result:.2f}")
#
# filtered_grades = {}
# for students_name, grade in students.items():
#     avg_grade = sum(grade) / len(grade)
#     if avg_grade >= 4.5:
#         filtered_grades[students_name] = avg_grade
# sorted_best_students = sorted(filtered_grades.items(), key=lambda kvp: kvp[1], reverse=True)
# for key, value in sorted_best_students:
#     print(f"{key} -> {value:.2f}")
#
