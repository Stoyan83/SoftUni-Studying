# command = input()
# judge = {}
# languages = []
#
# while not command == "exam finished":
#     current_command = command.split("-")
#
#     if current_command[1] == "banned":
#         new_key = None
#         judge[new_key] = judge.pop(current_command[0])
#
#     else:
#         user, language, score = command.split("-")
#         if user not in judge:
#             judge[user] = {"language": [language], "score": [score]}
#         else:
#             if judge[user]["score"][0] < score:
#                 judge[user]["score"] = score
#             if judge[user]["language"] != language:
#                 judge[user]["language"].append(language)
#                 judge[user]["score"].append(score)
#
#     command = input()
#
# print("Results:")
# for key, value in judge.items():
#     if key != None:
#         print(f"{key} | {max((value['score']))}")
#
# for key, value in judge.items():
#     languages += value["language"]
# print('Submissions:')
# unique_languages = set(languages)
# for s in sorted(unique_languages, key=lambda x: x, reverse=True):
#     n_l = languages.count(s)
#     print(f"{s} - ", end="")
#     print(n_l)
#


exam_submissions = {}
students = {}

while True:
    input_line = input()
    if input_line == 'exam finished':
        break

    command = input_line.split('-')
    username = command[0]
    language_action = command[1]

    if language_action != 'banned':
        if language_action not in exam_submissions:
            exam_submissions[language_action] = 0
        exam_submissions[language_action] += 1

        points = int(command[2])
        students[username] = max(students.get(username, 0), points)

    elif username in students:
        students.pop(username)

print('Results:')
for username, points in students.items():
    print(f"{username} | {points}")
print('Submissions:')
for language, submissions_count in exam_submissions.items():
    print(f'{language} - {submissions_count}')