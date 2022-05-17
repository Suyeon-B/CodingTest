# permutation 사용
import itertools


def permute(nums):
    return [list(perm) for perm in itertools.permutations(nums, len(nums))]


nums = [0, 1]
print(permute(nums))
