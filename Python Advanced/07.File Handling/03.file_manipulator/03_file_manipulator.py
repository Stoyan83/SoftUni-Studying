from os import path, remove

line = input()

while line != "End":

    line_parts = line.split("-")
    command = line_parts[0]
    file_name = line_parts[1]

    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        if path.exists(file_name):
            content = line_parts[2]
            with open(file_name, "a") as file:
                file.write(content + "\n")
    elif command == "Delete":

        if path.exists(file_name):
            remove(file_name)
        else:
            print("An error occurred")
    elif command == "Replace":
        old = line_parts[2]
        new = line_parts[3]
        if path.exists(file_name):

            with open(file_name, "r+") as file:
                new_file_content = file.read().replace(old, new)
                file.seek(0)
                file.truncate()
                file.write(new_file_content)
        else:
            print("An error occurred")

    line = input()