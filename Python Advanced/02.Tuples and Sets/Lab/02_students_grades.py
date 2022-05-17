number_of_students = int(input())
students = {}

for i in range(number_of_students):
    student, score =input().split()
    score = float(score)
    if student not in students:
        students[student] = []
    students[student].append(score)

for key, value in students.items():
    print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {sum(value)/len(value):.2f})")

