class Solution:
    def sortColors(self, nums): # A[0]~A[n-1]까지 insertion sort
        n = len(nums) 
        for i in range(1, n): # i = 1 ~ n-1까지,
            j = i-1 # j = 0 ~ n-2까지 (index j+1값, 즉 index n-1인 마지막 수 까지 비교하기 위함)
            while j >=0 and nums[j] > nums[j+1]: # index값 j가 0이상이고, 두 값을 비교했을 때 큰 값이 앞에 위치하면
                nums[j], nums[j+1] = nums[j+1], nums[j] # 자리를 바꿔주고
                j -= 1 # index값을 줄여가며 index [0]이 될 때 까지 앞에 큰 값이 있나 확인한다.
