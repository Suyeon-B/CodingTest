import collections
import operator
def largestNumber(nums):
    """
    숫자를 문자로 바꾸고 정렬 후 붙임
    자리수가 큰 수는 따로 저장함(맨 앞자리 수만 정렬하기 위해)
    """
    output = []
    temp = collections.defaultdict(list)
    for num in nums:
        while(num!=0):
            if num<10:
                output.append(num%10)
            # else:
            #     temp[num//((len(str(num))-1)*10)].append(num%((len(str(num))-1)*10))
            num //= 10
            

    output.sort(reverse=True)
    # temp = sorted(temp.items(), key=lambda k_v: k_v[1][2], reverse=True)
    nums.sort(reverse=True)
    n = nums[0]
    i = 0
    while nums:
        digit = (len(str(nums[i]))-1)*10
        if digit:
            for i in range(len(output)):
                if output[i] == n//digit and n>10:
                    output[i] = n 
                    nums.remove(n)
                    break

    return ''.join(map(str, output))

nums = [3,30,34,5,9]  
print(largestNumber(nums))
        