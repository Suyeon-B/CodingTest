# 반례 존재
# 투 포인터로 다시 풀어볼 것
import collections

def lengthOfLongestSubstring(s: str) -> int:
    cnt = collections.defaultdict(int)
    result = 0

    if len(set(s)) == 1:
        return 1

    for i in range(len(s)-1):
        cnt[s[i]] += 1
        if cnt[s[i]] > 1:
            cnt = collections.defaultdict(int)
            cnt[s[i]] += 1
            result = max(result, len(cnt.keys()))
            continue
    if s and s[-1] != s[-2]:
        cnt[s[-1]] += 1
    result = max(result, len(cnt.keys()))
    return result

s = "aab"
print(lengthOfLongestSubstring(s))
