def solution(s):
    """
    단위별로 다 try
    """
    answer = len(s)
    
    for window in range(1, len(s)//2+1):
        compressed = ""
        now = s[:window]
        cnt = 1
        for i in range(window, len(s), window):
            temp = s[i:i+window]
            if now == s[i:i+window]: # 동일한 문자열이 반복이라면
                cnt+=1
            else: # 다른 문자열이 나왔다면
                compressed += f'{cnt}{now}' if cnt >=2 else now
                cnt = 1
                now = s[i:i+window]
        compressed += f'{cnt}{now}' if cnt >=2 else now
        answer = min(len(compressed), answer)

    return answer

s = "aabbaccc"	 # 7

print(solution(s))