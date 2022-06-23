jobs = [int(x) for x in input().split(", ")]
searched_index = int(input())

target_job = jobs[searched_index]
cycles = 0

for i in range(len(jobs)):
    current_job = jobs[i]
    print(current_job)
    if current_job < target_job or current_job == target_job and searched_index >= i:
        cycles += current_job
        print(cycles)

print(cycles)
