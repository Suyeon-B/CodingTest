# 재귀를 이용한 풀이
from collections import Counter
from typing import List


def removeDuplicateLetters(s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


if __name__ == '__main__':
    s = "bbbacacca"
    print(removeDuplicateLetters(s))
