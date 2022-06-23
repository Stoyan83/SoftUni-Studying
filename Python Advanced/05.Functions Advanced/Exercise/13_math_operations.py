''''
The first element should be added to the value of the key "a"
The second element should be subtracted from the value of the key "s"
The third element should be divisor to the value of the key "d"
The fourth element should be multiplied by the value of the key "m"
Each result should replace the value of the corresponding key
You must repeat the same steps consecutively until you run out of numbers
'''
from collections import deque


def math_operations(*args, **kwargs):
    que = deque(args)
    result = ""
    a = 0
    while que:
        nums = []
        for i in range(4):
            if len(que) == 0:
                break
            nums.append((que.popleft()))

        try:
            kwargs["a"] = round(kwargs["a"] + nums[0], 1)
            kwargs["s"] = kwargs["s"] - nums[1]
            kwargs["d"] /= float(nums[2]) if nums[2] != 0 else kwargs["d"] == float(kwargs["d"])
            kwargs["m"] = round(kwargs["m"] * nums[3], 1)
        except:
            pass

    sorted_kwargs = sorted(kwargs.items(), key = lambda x: (-x[1], x[0]))
    for key, value in sorted_kwargs:
        value = f"{value:.1f}"
        result += f"\n{key}: {value}"

    return result




print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))


