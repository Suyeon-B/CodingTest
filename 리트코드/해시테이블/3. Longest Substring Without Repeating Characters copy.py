# 투 포인터 & 슬라이딩 윈도우
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    start = max_length = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index-start+1)
        used[char] = index
    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
