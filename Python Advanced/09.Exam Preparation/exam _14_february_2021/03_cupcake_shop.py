def stock_availability(boxes, *args ):
    if args[0] == "delivery":
        boxes.extend(args[1:])
    if args[0] == "sell":
        if len(args) == 1:
            boxes.pop(0)
        else:
            if isinstance(args[1],int):
                for _ in range(args[1]):
                    boxes.pop(0)
            else:
                for i in args[1:]:
                    if i in boxes:
                        while i in boxes:
                            boxes.remove(i)

    return boxes



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
