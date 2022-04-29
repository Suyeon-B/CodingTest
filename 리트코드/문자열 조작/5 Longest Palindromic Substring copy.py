"""
핵심 IDEA
    1. palindrome 글자는 짝수거나 홀수 두 경우 뿐이다.
        -> 따라서 짝수일 때와 홀수일 때를 각각 구해서 max값을 취한다.
    2. 짝수일 때와 홀수일 때 두 경우를 구하기 위해 투 포인터를 2번 돌린다. 
얻어갈 점
    1. 문자열이 같은지 보는 문제에서는 투포인터를 적극 활용하자.
    2. 특히 투 포인터를 2, 3 길이로 시작해 한 번에 돌려서, 조건에 맞으면 양쪽으로 확장하는 식으로 하면 효율적이다.
    3. python max함수는 key값으로 문자열의 len 값을 줄 수 있다.
"""


def longest_palindrome():
    s = "babad"

    def two_pointer(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    if len(s) < 2 or s == s[::-1]:
        return s
    result = ""
    for i in range(len(s)-1):
        result = max(result, two_pointer(i, i+1), two_pointer(i, i+2), key=len)
    return result


print(longest_palindrome())
