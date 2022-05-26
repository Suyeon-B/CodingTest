def solution(s):
    # 초기 답
    answer = 0

    # 초기 윈도우 사이즈
    unit = 1
    window = s[:unit]
    n = len(s)

    # 윈도우 사이즈별(1~n//2)로 전체를 순회한다.
    output = 0
    flag = False
    cnt = 1
    while unit <= n//2:
        for i in range(unit, n, unit):
            # 같으면 answer-=1
            temp = (s[i:i+unit], i)
            if window == s[i:i+unit]:
                # answer -= 1
                cnt += 1
                flag = True
            # 다르면 기준 이동
            else:
                temp2 = (s[i:i+unit], i)
                window = s[i:i+unit]
                if flag:
                    answer += len(str(cnt)) + unit
                    flag = False
                cnt = 0

        if flag:
            answer += len(str(cnt)) + unit

        unit += 1
        window = s[:unit]
        output = min(output, answer)
    return answer


s = "aabbaccc"
print(solution(s))
