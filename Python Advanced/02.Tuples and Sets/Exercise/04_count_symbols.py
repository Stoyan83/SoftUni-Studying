sequence = tuple(input())

for i in sorted(tuple(set(sequence))):
    print(f"{i}: {sequence.count(i)} time/s")
