number_of_queries = int(input())
num_stack = []

for _ in range(number_of_queries):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        num_stack.append(query[1])
    if num_stack:
        if query[0] == 2:
            num_stack.pop()
        elif query[0] == 3:
            print(max(num_stack))
        elif query[0] == 4:
            print(min(num_stack))

for _ in range(len(num_stack)):
    if len(num_stack) > 1:
        print(num_stack.pop(),  end= ", ")
    else:
        print(num_stack.pop())