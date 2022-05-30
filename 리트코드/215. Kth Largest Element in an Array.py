import heapq
def findKthLargest(nums, k):
    """
    최대힙
        - k번 뽑아서 출력하기만 하면 됨
    """
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
    result = 0
    for _ in range(k):
        result = -heapq.heappop(max_heap)
    return result

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))