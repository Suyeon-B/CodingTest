def maxSlidingWindow(nums, k):
    l, r = 0, k
    output = []
    while r <= len(nums):
        output.append(max(nums[l:r]))
        l+=1
        r+=1

    return output


nums = [1]
k = 1
print(maxSlidingWindow(nums, k))