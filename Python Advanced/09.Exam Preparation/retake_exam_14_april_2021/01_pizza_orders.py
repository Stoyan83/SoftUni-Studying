from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employee_capacity = [int(x) for x in input().split(", ")]

total_pizzas = 0

while pizza_orders and employee_capacity:
    current_order = pizza_orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue
    current_employee_capacity = employee_capacity.pop()
    if current_employee_capacity >= current_order:
        total_pizzas += current_order
        continue
    if current_employee_capacity < current_order:
        current_order -= current_employee_capacity
        total_pizzas += current_employee_capacity
        pizza_orders.appendleft(current_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employee_capacity:
        print("Employees: ", end="")
        print(*employee_capacity, sep=", ")

else:
    print("Not all orders are completed.")
    print(f"Orders left: ", end="")
    print(*pizza_orders, sep=", ")
