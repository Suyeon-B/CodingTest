# 중복 값 pass해서 TLE 해결
# i 값 뒤만 보는 방법으로 최적화 retry 해볼 것
def main():
    nums = []
    if len(nums) < 3:
        return nums

    left, right = 0, len(nums)-2
    triplets_sum = 0
    triplets = []
    arr = result = []
    nums = sorted(nums, reverse=True)

    for i in range(len(nums)):
        curr = nums[i]
        arr = nums[:i]+nums[i+1:]

        if i > 0 and nums[i] == nums[i-1]:
            continue

        while left < right:
            triplets_sum = arr[left] + arr[right]
            if triplets_sum + curr == 0:
                result = sorted([curr, arr[left], arr[right]])
                triplets.append(tuple(result))
                left += 1
                right -= 1
            elif triplets_sum + curr > 0:  # sum값을 줄여야 함
                left += 1
            else:
                right -= 1
        left, right = 0, len(nums)-2

        triplets = list(set(triplets))
        triplets = [list(triplet) for triplet in triplets]
        return triplets


print(main())
