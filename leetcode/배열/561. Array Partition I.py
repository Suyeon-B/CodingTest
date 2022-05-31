from typing import List

# 정렬 후 두개씩 묶어서 최솟값을 더하면 최댓값을 만들 수 있음


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    sum = 0
    pair = []
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))
