from collections import deque

boxes = [int(m) for m in input().split()]
magic_level = deque(int(v) for v in input().split())

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

crafted_presents = {}

doll_and_a_train = 0
bear_and_bicycle = 0
pairs = {
    1: ['Doll', 'Wooden train'],
    2: ['Teddy bear', 'Bicycle'],
}

while boxes and magic_level:
    material = boxes.pop()
    magic = magic_level.popleft()

    if material == 0 and magic == 0:
        continue

    if material == 0:
        magic_level.appendleft(magic)
        continue

    if magic == 0:
        boxes.append(material)
        continue

    product = material * magic
    if product in presents.keys():
        present = presents[product]
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
        if present in pairs[1]:
            doll_and_a_train += 0.5
        elif present in pairs[2]:
            bear_and_bicycle += 0.5
        continue

    if product < 0:
        boxes.append(material + magic)
        continue

    boxes.append(material + 15)

if doll_and_a_train >= 1 or bear_and_bicycle >= 1:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if boxes:
    print(f'Materials left: {", ".join(str(m) for m in reversed(boxes))}')
if magic_level:
    print(f'Magic left: {", ".join(str(m) for m in magic_level)}')

for toy, quantity in sorted(crafted_presents.items()):
    print(f'{toy}: {quantity}')