command = input()
usernames = {}

while not command == "Log out":
    current_command = command.split(": ")

    if current_command[0] == "New follower":
        username = current_command[1]
        if username not in usernames:
            usernames[username] = [0, 0]

    elif current_command[0] == "Like":
        username = current_command[1]
        like_count = int(current_command[2])
        if username not in usernames:
            usernames[username] = [like_count, 0]
        else:
            usernames[username][0] += like_count

    elif current_command[0] == "Comment":
        username = current_command[1]
        if username not in usernames:
            usernames[username] = [0, 1]
        else:
            usernames[username][1] += 1

    elif current_command[0] == "Blocked":
        username = current_command[1]
        if username not in usernames:
            print(f"{username} doesn't exist.")
        else:
            usernames.pop(username)

    command = input()
print(f"{len(usernames)} followers")
for key, value in usernames.items():
    print(f"{key}: {value[0] + value[1]}")
