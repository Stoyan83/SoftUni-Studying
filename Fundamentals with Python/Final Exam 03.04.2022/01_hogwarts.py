spell = input()

command = input()

while not command == "Abracadabra":
    current_command = command.split()

    if current_command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif current_command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif current_command[0] == "Illusion":
        index = int(current_command[1])
        letter = current_command[2]
        if index not in range(len(spell)):
            print("The spell was too weak.")

        else:
            left = spell[:index]
            right = spell[index + 1:]
            spell = left + letter + right
            print("Done!")

    elif current_command[0] == "Divination":
        first_substring = current_command[1]
        second_substring = current_command[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif current_command[0] == "Alteration":
        substring = current_command[1]
        if substring in spell:
            index = spell.find(substring)
            left = spell[:index]
            right = spell[index + len(substring):]
            spell = left + right
            print(spell)

    else:
        print("The spell did not work!")

    command = input()
