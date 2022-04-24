# 빈도수가 엄청 클 때 문제가 생기는 코드
import sys, collections # defaultdict, Counter import
sys.stdin = open("Baekjoon/Greedy/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())
strings = []

temp = ''
for i in range(n):
    string = input().strip()
    strings.append(string)

    # 문자열을 세어주는 용도로 string을 합쳐준다.
    temp += string

# 입력된 문자열의 빈도수를 세어준다.
alpha_freq = collections.Counter(temp)

# 입력된 문자열의 자릿수를 계산해 dict[문자] = (자릿수, 빈도수) 형태로 저장한다.
Alpha = collections.defaultdict(list)
for string in strings:
    for chr in string:
        idx = len(string) - string.index(chr) - 1
        string = string[1:]
        # 만약 자리수가 이미 채워진 문자라면, (더 큰 자릿수, 빈도수, 다음 자릿수, 다음 자릿수 ...) 순서로 넣는다. -> sort 인덱싱 위해
        if not Alpha[chr]:
            Alpha[chr] = [idx, alpha_freq[chr]]
        else:
            if len(Alpha[chr]) < 2:
                Alpha[chr] = [max(idx, Alpha[chr][0]), alpha_freq[chr]] + [idx]
            else: # 2번 이상 사용된 문자라면
                new_top = max(idx, Alpha[chr][0])
                bottom = min(idx, Alpha[chr][0])
                Alpha[chr][0] = new_top
                Alpha[chr] += [bottom]

# 자릿수 높은 애로 sort -> 빈도수로 sort 후 나온 순서대로 9~0까지 할당
sorted_by_digit = dict(sorted(Alpha.items(), key=lambda item: item[0], reverse=True))
sorted_by_freq = dict(sorted(sorted_by_digit.items(), key=lambda item: item[1], reverse=True))

chrs = sorted_by_freq.keys()

points = collections.defaultdict(int)
p = 9
for chr in chrs:
    points[chr] = p
    p-=1

# 합 계산
total = 0
for chr in temp:
    # 여러번 나온 문자라면 한번에 처리하고 다음 것 부터는 연산에 추가하지 않는다.
    if len(sorted_by_freq[chr])>2:
        sorted_by_freq[chr].pop(1)
        total += points[chr] * (10**sorted_by_freq[chr].pop(0))
        while sorted_by_freq[chr]:
            total += points[chr] * (10**sorted_by_freq[chr].pop())
    # 한번 나온 문자면
    else:
        if sorted_by_freq[chr]:
            total += points[chr] * (10**sorted_by_freq[chr][0])

print(total)