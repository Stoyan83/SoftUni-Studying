def loading_bar(num):
    progress = ["%"] * 10
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{num}% [{'%' * (num // 10)}{'.' * (10 - num // 10)}]\nStill loading..."


number = int(input())
print(loading_bar(number))