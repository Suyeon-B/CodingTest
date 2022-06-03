def search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        m = l + (r-l)//2

        if nums[m] == target:
            return m
        
        if nums[l] <= nums[m]: # '왼쪽 처음 수 <= 중간 수' 이면, 왼쪽 부분은 모두 정렬된 상태
            if nums[l] <= target <= nums[m]: # 정렬된 수들 안에 target이 있나 확인
                # 있으면
                r = m-1
            else:
                l = m+1
        else: # 왼쪽이 정렬되지 않은 상태면 오른쪽은 무조건 정렬된 상태
            if nums[m] <= target <= nums[r]: # 정렬된 수들 안에 target이 있나 확인
                # 있으면
                l = m+1
            else:
                r = m-1
         
    return -1

nums = [4,5,6,7,0,1,2]
target = 4
print(search(nums, target))
        