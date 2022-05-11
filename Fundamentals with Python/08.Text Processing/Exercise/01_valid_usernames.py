# user_names = input().split(", ")
#
# for user in user_names:
#     if len(user) >= 3 and len(user) <= 16:
#         if user.isalnum() or "-" in user or "_" in user:
#             for ch in user:
#                 if ch == " ":
#                     continue
#             print(user)

def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def type_of_ch(username):
    for ch in username:
        if not(ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True


def redundant(username):
    for ch in username:
        if ch == " ":
            return False
    return True


def username_is_valid(username):
    if length(username) and type_of_ch(username) and redundant(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

