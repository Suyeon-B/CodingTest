def minWindow(s, t):
    """
    왼쪽, 오른쪽으로 나누어 탐색
        if 왼쪽-1 ~ 오른쪽-1 포함:
            다음 윈도우는 s[1:-1]
        elif 왼쪽 -1에 포함:
            다음 윈도우는 s[1:]
        else:
            s[:-1]
    """
    t_list = list(t)
    l, r = 1, len(s)-1
    f = True
    while True:
        l, r = l+1, r-1 
        for t in t_list:
            if len(s) == len(t):
                return s
            if f:
                temp = s
                f = False
            left = s[l:].find(t)
            right = s[:r].find(t)
            if left>-1 and right>-1:
                s = s[l:r]
            elif left>-1:
                s = s[l:]
            elif right>-1:
                s = s[:r]
            else:
                s = temp
                f = True
                break
        return s

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))