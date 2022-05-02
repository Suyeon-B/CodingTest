# 투 포인터로 다시 풀기
def main():
    nums = [-1, 0, 1, 2, -1, -4]
    if len(nums) < 3:
        return nums

    left, right = 0, len(nums)-1
    triplets_sum = 0
    triplets = []
    nums = sorted(nums, reverse=True)

    while left < right:
        triplets_sum += nums[left] + nums[right]

        if triplets_sum < 0:
            right -= 1
            triplets_sum = 0
            continue
        else:
            if triplets_sum == 0:
                if 0 in nums[left:]:
                    triplets.insert(0, 1)
                else:
                    triplets_sum = 0
                    triplets = []
                    continue
            else:
                right -= 1
                if triplets_sum + nums[right] != 0:
                    right -= 1
                    continue
                else:
                    triplets.insert(nums[right], 1)
                    triplets_sum = 0
                    triplets = []
                    left += 1
                    right = len(nums)-1
                    continue


main()
