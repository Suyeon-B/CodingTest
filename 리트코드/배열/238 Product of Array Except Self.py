# space complexity O(1)로 retry 해보기
import collections


def main():
    nums = [1, 2, 3, 4]
    prefix = collections.deque([1])
    suffix = [1]

    # get prefix
    for i in range(1, len(nums)):
        result = prefix[-i]*nums[-i]
        prefix.appendleft(result)
    # get suffix
    for i in range(1, len(nums)):
        result = suffix[i-1]*nums[i-1]
        suffix.append(result)

    result = []
    for i in range(len(nums)):
        result.append(prefix[i]*suffix[i])

    return result


print(main())
