command = input().split("-")
phonebook = {}

while len(command) > 1:
    phonebook[command[0]] = command[1]

    command = input().split("-")

searches_num = command[0]
for search in range(int(searches_num)):
    contact = input()
    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")


