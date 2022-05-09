from typing import List
from itertools import combinations


def arrayPairSum(nums: List[int]) -> int:
    comb = list(combinations(nums, 2))
    print(comb)


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    arrayPairSum(nums)
