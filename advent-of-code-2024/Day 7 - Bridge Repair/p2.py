from itertools import product
from tqdm import tqdm
with open('data.txt', 'r') as file:
    data = file.read().splitlines()

result = 0
for d in data:
    values = d.split()
    target = int(values[0][:-1])
    nums = list(map(int, values[1:]))
    def check(ops):
        result = nums[0]
        for i in range(1, len(nums)):
            if ops[i-1] == "+":
                result += nums[i]
            elif ops[i - 1] == "|":
                result = int(f"{result}{nums[i]}")
            else:
                result *= nums[i]
            # print(f"{nums[i - 1]} {op[i-1]} {nums[i]} = {result}")
        return result

    for op in tqdm(product("+*|", repeat=len(nums)-1)):
        if check(op) == target:
            result += target
            break
print(result)