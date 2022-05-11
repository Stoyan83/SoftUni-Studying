import re


def dec_count(message):
    dec_ch = ["s", "S", "t", "T", "a", "A", "r", "R"]
    count = 0
    for ch in message:
        if ch in dec_ch:
            count += 1
    return count


number = int(input())
des_planet = []
att_planet = []

pattern = "@([A-Za-z]+)([^@\-\!\:\>]+)?:(\d+)([^@\-\!\:\>]+?)\!([AD])\!([^@\-\!\:\>]+)?->(\d+)"

for m in range(number):
    message = input()
    new_message = "".join([chr(ord(x) - dec_count(message)) for x in message])
    matches = re.finditer(pattern, new_message)
    for m in matches:
        if m.group(5) == "D":
            des_planet.append(m.group(1))

        else:
            att_planet.append(m.group(1))

print(f"Attacked planets: {len(att_planet)}")
if len(att_planet) > 0:
    for p in sorted(att_planet):
        print(f"-> {p}")
print(f"Destroyed planets: {len(des_planet)}")
if len(des_planet) > 0:
    for p1 in sorted(des_planet):
        print(f"-> {p1}")
