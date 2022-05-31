# space complexity O(1)
# prefix, suffix를 바로 output 배열에 반영
import collections


def main():
    nums = [1, 2, 3, 4]
    n = len(nums)
    prefix = 1
    output = []

    # get prefix
    for i in range(n):
        output.append(prefix)
        prefix *= nums[i]
    # get suffix
    prefix = 1
    for i in range(n-1, -1, -1):
        output[i] *= prefix
        prefix *= nums[i]

    return output


print(main())
