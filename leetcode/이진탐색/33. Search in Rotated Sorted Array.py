def search(nums, target):
    # 가장 작은 수의 인덱스를 먼저 찾는다.
    l, r = 0, len(nums)-1
    while l<r:
        m = l + (r-l)//2
        if nums[m]>nums[r]:
            l = m+1
        else:
            r = m
    
    # l(=r)은 가장 작은 수의 인덱스이자, rotate의 기준 숫자이다.
    rotate = l
    l, r = 0, len(nums)-1
    while l<=r:
        m = l + (r-l)//2
        realmid = (m+rotate)%len(nums) # 왜?????
        '''
        For those who struggled to figure out 
        why it is realmid=(mid+rot)%n: 
            you can think of it this way:
                If we want to find realmid for array [4,5,6,7,0,1,2], 
                you can shift the part before the rotating point to the end of the array (after 2) 
                so that the sorted array is "recovered" from the rotating point but only longer, 
                like this: [4, 5, 6, 7, 0, 1, 2, 4, 5, 6, 7]. 
                The real mid in this longer array is the middle point between the rotating point and 
                the last element: (rot + (hi+rot)) / 2. 
                (hi + rot) is the index of the last element. 
                And of course, this result is larger than the real middle. 
                So you just need to wrap around and get the remainder: ((rot + (hi + rot)) / 2) % n. 
                And this expression is effectively (rot + hi/2) % n, which is (rot+mid) % n.
        '''
        if nums[realmid] == target:
            return realmid
        elif nums[realmid] < target:
            l = m + 1
        else:
            r = m-1
    
    return -1

nums = [4,5,6,7,0,1,2]
target = 4
print(search(nums, target))
        