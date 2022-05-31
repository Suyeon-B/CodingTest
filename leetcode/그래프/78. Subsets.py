# combination 사용
from itertools import combinations


def subsets(nums):
    nums.sort()
    output = []
    for i in range(len(nums)+1):
        temp = list(combinations(nums, i))
        for t in temp:
            output.append(list(t))

    return output


nums = [1, 2, 3]
print(subsets(nums))
