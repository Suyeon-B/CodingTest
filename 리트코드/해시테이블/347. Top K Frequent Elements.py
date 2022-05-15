from collections import Counter
def topKFrequent(nums, k):
    cnt = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
    return [cnt[i][0] for i in range(k)]


nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))