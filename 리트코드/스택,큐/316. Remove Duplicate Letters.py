# 버그 처리 필요
from collections import Counter
from typing import List


def removeDuplicateLetters(s: str) -> str:
    list_s = list(s)
    cnt = Counter(list_s)
    output = ""

    # 지우는 기준
    # 1) cnt > 1
    # 2) 뒤에 더 뒷 순번인 알파벳이 있고,
    #    그 사이에 앞 순번 알파벳이 없으면 안자움 (output에 추가)
    for i in range(len(list_s)-1):
        if cnt[list_s[i]] == 1:  # 하나 밖에 없으면 output에 추가
            output += list_s[i]
            cnt[list_s[i]] -= 1
            continue
        elif cnt[list_s[i]] > 1:  # 두 개 이상일 때
            # 뒤에 더 뒷 순번인 알파벳이 있고
            if sorted(list_s[i+1:])[-1] > list_s[i]:
                idx = len(list_s)-1-list(reversed(list_s)
                                         ).index(sorted(list_s[i+1:])[-1])
                # 그 사이에 앞 순번 알파벳이 없으면 안 지움
                if sorted(list_s[i:idx+1])[0] > list_s[i]:
                    output += list_s[i]
                    cnt[list_s[i]] = 0
                    continue
                else:
                    cnt[list_s[i]] -= 1
            else:
                cnt[list_s[i]] -= 1
    if cnt[list_s[-1]] > 0:  # 하나 밖에 없으면 output에 추가
        output += list_s[-1]

    return output


if __name__ == '__main__':
    s = "bbbacacca"
    print(removeDuplicateLetters(s))
