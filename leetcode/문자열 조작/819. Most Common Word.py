# maketrans, translate를 이용한 풀이
from typing import List
from collections import Counter


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = paragraph.maketrans({
        '.': ' ',
        ',': ' ',
        '!': ' ',
        '?': ' ',
        ';': ' ',
        "'": " "
    })

    common_cnt = Counter(paragraph.translate(
        words).lower().split()).most_common()
    output = common_cnt.pop(0)[0]
    if len(banned) == 0:
        return output
    while output in banned:
        output = common_cnt.pop(0)[0]
    return output


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(mostCommonWord(paragraph, banned))
