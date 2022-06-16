import re


def solution(s):
    # 문자열 파싱
    s = s.split("},{")
    s[0] = str(s[0]).replace("{{", "")
    s[-1] = str(s[-1]).replace("}}", "")

    # 길이순 정렬
    s.sort(key=len)

    for i in range(len(s)):
        s[i] = [s[i].split(",")]

    # 앞에서부터 없는 문자 추가
    answer = []
    for num in s:
        for sub in num:
            for ss in sub:
                if ss not in answer:
                    answer.append(ss)
    
    return list(map(int, answer))

s = "{{20,111},{111}}"	
print(solution(s))