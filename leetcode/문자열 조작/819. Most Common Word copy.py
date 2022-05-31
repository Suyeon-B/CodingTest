# 정규식을 활용한 풀이
import re
from typing import List
from collections import Counter


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(
        r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    common_cnt = Counter(words)
    return common_cnt.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(mostCommonWord(paragraph, banned))
