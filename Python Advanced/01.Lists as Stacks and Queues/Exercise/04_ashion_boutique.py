clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
initial_capacity = 0
racks = 1

while clothes_stack:
    current_piece = clothes_stack.pop()
    if current_piece <= rack_capacity - initial_capacity:
        initial_capacity += current_piece
    else:
        racks += 1
        initial_capacity = current_piece

print(racks)