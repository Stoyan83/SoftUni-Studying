population = [int(el) for el in input().split(',')]
min_wealth = int(input())
equal = True

for num in population:
    if num < min_wealth:
        if max(population) <= min_wealth:
            print("No equal distribution possible")
            equal = False
            break
        min_index = population.index(num)
        population[min_index] = min_wealth
        diff = min_wealth - num
        index = population.index(max(population))
        population[index] = max(population) - diff

if equal:
    print(population)
